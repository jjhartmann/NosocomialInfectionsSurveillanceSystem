from django.contrib.auth.decorators import login_required
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
    return render(request, 'basic_search/index.html', {'user': user, 'countries': countries, 'segments': segments})


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

        # the country
        cntry = post['country']
        if not cntry == 'ALL':
            keywordlist.update({'country': post['country']})

        # complete seg
        cseg = find_complete_segment(post['complete_seq'])
        if not cseg == 'all':
            keywordlist.update({'completeness': cseg})

        # genbank accession number
        genbank_an = post['genbank_na_accnum']
        if not genbank_an == '':
            keywordlist.update({'genbank_accession_number': genbank_an})

        # genome segment
        genomeseg = find_genome_segment(post['genomesegment_or_proteinname'])
        if not genomeseg == 'all':
            keywordlist.update({'genomesegment_or_proteinname': genomeseg})

        # subtype
        subtype = post['subtype']
        if not subtype == '':
            keywordlist.update({'subtype': subtype})

        # virus_name
        virus_name = post['virus_name']
        if not subtype == '':
            keywordlist.update({'virus_name': virus_name})

        # virus_type
        virus_type = find_virus_type(post['virus_type'])
        if not virus_type == 'all':
            asdf = 123
            # do something for the virus type

        # from year to year
        fromyear = post['fromyear']
        toyear = post['toyear']
        if not (fromyear == '' or toyear == ''):
            do_something_here = 0
            # create filter for data.

        query_entries_na = Influenza_NA.objects.filter(**keywordlist)
        query_entries_aa = Influenza_AA.objects.filter(**keywordlist)


        return render(request, "basic_search/details.html", {'queryEntriesNA': query_entries_na, 'queryEntriesAA': query_entries_aa})
    else:
        return render_to_response(reverse('basic_search:index'), {}, context)


# details view
