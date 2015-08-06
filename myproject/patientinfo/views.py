from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .models import *
from forms import PatientinfoForm

from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf

# Create your views here.

@login_required
def index(request, username):
    return render(request, 'patientinfo/index.html', {'patientinfos': Patientinfo.objects.all(),'username': username })

def detail(request, username, patientinfo_id):
    return render(request, 'patientinfo/detail.html', {'patientinfo': Patientinfo.objects.get(id=patientinfo_id),'username': username })

def create(request, username):
    if request.POST:
        form = PatientinfoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('patientinfo:index', kwargs={'username': username }))
    else:
        form = PatientinfoForm()

    args = {}
    args.update(csrf(request))

    args['form']=form
    args['username']=username
    return render(request, 'patientinfo/create_orig.html', args)

def update(request, username, patientinfo_id):
    record = get_object_or_404(Patientinfo, id=patientinfo_id)
    
    if request.POST:
        form = PatientinfoForm(request.POST or None,instance=record)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('patientinfo:index', kwargs={'username': username}))
    else:
        form = PatientinfoForm(instance=record)

        args = {}
        args.update(csrf(request))

        args['form']=form
        args['username']=username
        args['patientinfo']=Patientinfo.objects.get(id=patientinfo_id)
    return render(request, 'patientinfo/update.html', args)
# def upload_index(request, username):
#     return render(request, 'patientinfo/upload_index.html', {'patientinfos': Patientinfo.objects.all(),'username': username })

# def upload(request, username):
#     if request.POST:
#         form = PatientDataForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()

#             return HttpResponseRedirect(reverse('patientinfo:index', kwargs={'username': username }))
#     else:
#         form = PatientDataForm()

#     args = {}
#     args.update(csrf(request))

#     args['form']=form
#     args['username']=username
#     return render(request, 'patientinfo/upload.html', args)

def delete(request, username, patientinfo_id):
    record = Patientinfo.objects.get(id=patientinfo_id)
    record.delete()
    return render(request, 'patientinfo/delete.html', {'username': username})
    

