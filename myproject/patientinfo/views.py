from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .models import *
from forms import PatientinfoForm
from forms import PatientDataForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.models import User


# Create your views here.

@login_required
def index(request, username):
    return render(request, 'patientinfo/index.html', {'patientinfos': Patientinfo.objects.all(), 'username': username})

@login_required
def mypatients(request, username):
    patients = Patientinfo.objects.filter(doctor=request.user.id)
    return render(request, 'patientinfo/index.html', {'patientinfos': patients, 'username': username})


@login_required
def index_data(request, username):
    return render(request, 'patientinfo/index_data.html',
                  {'patientinfos': Patientinfo.objects.all(), 'username': username})


@login_required
def index_manage(request, username):
    return render(request, 'patientinfo/index_manage.html',
                  {'patientinfos': Patientinfo.objects.all(), 'username': username})


def detail(request, username, patientinfo_id):
    return render(request, 'patientinfo/detail.html',
                  {'patientinfo': Patientinfo.objects.get(id=patientinfo_id), 'username': username})


def create(request, username):
    if request.POST:
        form = PatientinfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['doctor'] = request.user.id
            form.save()

            return HttpResponseRedirect(reverse('patientinfo:index', kwargs={'username': username}))
    else:
        form = PatientinfoForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form
    args['username'] = username
    return render(request, 'patientinfo/create.html', args)


def update(request, username, patientinfo_id):
    record = get_object_or_404(Patientinfo, id=patientinfo_id)

    if request.POST:
        form = PatientinfoForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('patientinfo:index', kwargs={'username': username}))
    else:
        form = PatientinfoForm(instance=record)

        args = {}
        args.update(csrf(request))

        args['form'] = form
        args['username'] = username
        args['patientinfo'] = Patientinfo.objects.get(id=patientinfo_id)
    return render(request, 'patientinfo/update.html', args)


def delete(request, username, patientinfo_id):
    record = Patientinfo.objects.get(id=patientinfo_id)
    record.delete()
    return render(request, 'patientinfo/delete.html', {'username': username})


def viewdata(request, username, patientinfo_id):
    return render(request, 'patientinfo/viewdata.html',
                  {'patientinfo': Patientinfo.objects.get(id=patientinfo_id), 'username': username})


def uploaddata(request, username, patientinfo_id):
    record = get_object_or_404(Patientinfo, id=patientinfo_id)

    if request.POST:
        form = PatientDataForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('patientinfo:index_data', kwargs={'username': username}))
    else:
        form = PatientDataForm(instance=record)

        args = {}
        args.update(csrf(request))

        args['form'] = form
        args['username'] = username
        args['patientinfo'] = Patientinfo.objects.get(id=patientinfo_id)
    return render(request, 'patientinfo/uploaddata.html', args)
