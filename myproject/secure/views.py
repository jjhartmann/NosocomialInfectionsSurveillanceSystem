from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext


# Create your views here.

@login_required
def indexview(request, username):
    return render(request, 'secure/index.html', {'username': username})
