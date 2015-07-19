from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views import generic
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from .models import Influenza_AA


# Create your views here.

# Index view to render the main project page
@login_required
def indexView(request, username):
    user = request.user;
    return render(request, 'basic_search/index.html', {'user': user})


@login_required
def process_search(request, username):
    context = RequestContext(request)

    if request.method == 'POST':
        return HttpResponse("something goes heere")
    else:
        return render_to_response(reverse('basic_search:index'), {}, context)
