from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views import generic
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from .models import *


# Create your views here.

# Index view to render the main project page
@login_required
def indexView(request, username):
    user = request.user;
    countries = COUNTRIES;
    segments = SEGMENTS;
    return render(request, 'basic_search/index.html',
                  {'user': user, 'countries': countries, 'segments': segments, 'username': username})


def find_complete_segment(x):
    return {
        '1': 'c',
        '2': 'nc',
        '3': 'p',
        '0': 'all',
    }.get(x, 'all')


def find_genome_segment(x):
    return {
        '1': 'PB2',
        '2': 'PB1',
        '3': 'PA',
        '4': 'HA',
        '5': 'NP',
        '6': 'NA',
        '7': 'M',
        '8': 'NS',
    }.get(x, 'all')


def find_virus_type(x):
    return {
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
    }.get(x, 'all')


@login_required
def process_search(request, username):
    context = RequestContext(request)

    if request.method == 'POST':
        keywordlist = {}
        post = request.POST

        # complete seg
        cseg = find_complete_segment(post['complete_seq'])
        if not cseg == 'all':
            keywordlist.update({'completeness__contains': cseg})

        # genbank accession number
        genbank_an = post['genbank_na_accnum']
        if not genbank_an == '':
            keywordlist.update({'genbank_accession_number': genbank_an})

        # subtype
        subtype = post['subtype']
        if subtype != '':
            keywordlist.update({'subtype__contains': subtype})

        # virus_name
        virus_name = post['virus_name']
        if virus_name != '':
            keywordlist.update({'virus_name__contains': virus_name})

        # First filter
        query_entries_na = Influenza_NA.objects.filter(**keywordlist)
        query_entries_aa = Influenza_AA.objects.filter(**keywordlist)

        # the country
        cntrylist = post.getlist('country')
        if not cntrylist[0] == 'ALL':
            queries = [Q(country=cntry) for cntry in cntrylist]

            query = queries.pop()
            for item in queries:
                query |= item

            query_entries_na = query_entries_na.filter(query)
            query_entries_aa = query_entries_aa.filter(query)

        # genome segment
        # genomeseg = find_genome_segment(post['genomesegment_or_proteinname'])
        gemomeseq_list = post.getlist('genomesegment_or_proteinname')
        if not gemomeseq_list[0] == 'all':
            queries = [Q(genomesegment_or_proteinname__contains=find_genome_segment(gemomeseq)) for gemomeseq in gemomeseq_list]

            query = queries.pop()
            for item in queries:
                query |= item

            query_entries_aa = query_entries_aa.filter(query)

            # Seperate protein names
            queries = [Q(genomesegment_or_proteinname__contains=gemomeseq) for gemomeseq in gemomeseq_list]

            query = queries.pop()
            for item in queries:
                query |= item

            query_entries_na = query_entries_na.filter(query)


        # virus_type
        keywordlist_other = {}
        virus_type = find_virus_type(post['virus_type'])
        if not virus_type == 'all':
            virus_type = "Influenza " + virus_type + " virus"
            keywordlist_other.update({'virus_name__contains': virus_type})

        # from year to year
        fromyear = post['fromyear']
        toyear = post['toyear']
        if (fromyear != '' or toyear != ''):
            # create filter for date
            if (fromyear != '' and toyear == ''):
                query_entries_na = query_entries_na.filter(date_discovered__gt=fromyear + "-01-01")
                query_entries_aa = query_entries_aa.filter(date_discovered__gt=fromyear + "-01-01")

            elif (fromyear == '' and toyear != ''):
                query_entries_na = query_entries_na.filter(date_discovered__lt=toyear + "-12-31")
                query_entries_aa = query_entries_aa.filter(date_discovered__lt=toyear + "-12-31")

            else:
                query_entries_na = query_entries_na.filter(
                    date_discovered__range=[fromyear + "-01-01", toyear + "-12-31"])
                query_entries_aa = query_entries_aa.filter(
                    date_discovered__range=[fromyear + "-01-01", toyear + "-12-31"])

        query_entries_na = query_entries_na.filter(**keywordlist_other)
        query_entries_aa = query_entries_aa.filter(**keywordlist_other)

        return render(request, "basic_search/details.html",
                      {'queryEntriesNA': query_entries_na, 'queryEntriesAA': query_entries_aa, 'username': username})
    else:
        return render_to_response(reverse('basic_search:index'), {}, context)

# details view
