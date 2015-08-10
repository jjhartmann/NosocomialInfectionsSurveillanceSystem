from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from patientinfo.models import Patientinfo
from basic_search.models import Influenza_AA, Influenza_NA
from nocoblast.models import FASTATable
import json


@login_required
def indexview(request, username):
    args = {}
    args['username'] = username
    args['mypatient_count'] = Patientinfo.objects.filter(doctor=request.user.id).count()
    args['database_entries'] = Influenza_AA.objects.all().count() + Influenza_NA.objects.all().count()
    args['blast_queries'] = FASTATable.objects.all().count()

    gender_donut = {}
    gender_donut['element'] = 'gender-moris-donut'
    gender_donut['data'] = []
    gender_donut['data'].append({'label': "Male", 'value': Patientinfo.objects.filter(gender='M').count()})
    gender_donut['data'].append({'label': "Female", 'value': Patientinfo.objects.filter(gender='F').count()})
    # gender_donut['data'][0]['label'] = 'Male'
    # gender_donut['data'][0]['value'] = Patientinfo.objects.filter(gender='M').count()
    # gender_donut['data'][1] = []
    # gender_donut['data'][1]['label'] = 'Female'
    # gender_donut['data'][1]['label'] = Patientinfo.objects.filter(gender='F').count()

    args['gender_donut'] = json.dumps(gender_donut)

    args['male_count'] = Patientinfo.objects.filter(gender='M').count()
    args['female_count'] = Patientinfo.objects.filter(gender='F').count()

    # Age metrics
    args['age1'] = Patientinfo.objects.filter(age__lte=10, age__gte=0).count()
    args['age2'] = Patientinfo.objects.filter(age__lte=20, age__gte=11).count()
    args['age3'] = Patientinfo.objects.filter(age__lte=30, age__gte=21).count()
    args['age4'] = Patientinfo.objects.filter(age__lte=40, age__gte=31).count()
    args['age5'] = Patientinfo.objects.filter(age__lte=50, age__gte=41).count()
    args['age6'] = Patientinfo.objects.filter(age__lte=60, age__gte=51).count()
    args['age7'] = Patientinfo.objects.filter(age__lte=70, age__gte=61).count()
    args['age8'] = Patientinfo.objects.filter(age__gte=71).count()


    # Host metrics
    args['host_human'] = Influenza_NA.objects.filter(host="Human").count() + Influenza_AA.objects.filter(
        host="Human").count()
    args['host_avian'] = Influenza_NA.objects.filter(host="Avian").count() + Influenza_AA.objects.filter(
        host="Avian").count()
    args['host_swine'] = Influenza_NA.objects.filter(host="Swine").count() + Influenza_AA.objects.filter(
        host="Swine").count()
    args['host_other'] = Influenza_NA.objects.all().count() + Influenza_AA.objects.all().count() - (
        args['host_human'] + args['host_avian'] + args['host_swine'])


    # Country Metrics
    args['country_count_NA'] = Influenza_NA.objects.values("country").annotate(Count("genbank_accession_number"))
    args['country_count_AA'] = Influenza_AA.objects.values("country").annotate(Count("genbank_accession_number"))

    return render(request, 'secure/index.html', args)
