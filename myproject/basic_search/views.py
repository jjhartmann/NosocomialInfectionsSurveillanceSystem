from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views import generic
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from .models import Influenza_AA


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'basic_search/index.html'
    context_object_name = 'influenz_aa'

    def get_queryset(self):
        return Influenza_AA;


# Index view to render the main project page
@login_required
def indexView(request, username):
    user = request.user;
    return render(request, 'basic_search/index.html', {'user': user})

