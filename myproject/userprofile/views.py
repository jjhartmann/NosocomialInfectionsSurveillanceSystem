from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from forms import UserProfileForm

#Create your views here.

@login_required
def set_profile (request, username):
    
    if request. method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userprofile:viewprofile', kwargs={'username': username}))
    else:
        
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance = profile)

    args = {}
    args.update(csrf(request))

    args['form']=form 
    args['username']=username
    return render(request, 'userprofile/setprofile.html', args)


@login_required
def view_profile (request, username):
    profile = request.user.profile
    return render(request, 'userprofile/viewprofile.html', {'userprofile': profile,'username': username })
   
