from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext


# Create your views here.


# Main function to call the index for the main front page.


def indexview(request):
    return render(request, 'index/index.html')


def loginview(request):
    return render(request, 'index/login.html')


def doctor_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index:index'))


def doctor_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use django's built in authentication
        userprofile = authenticate(username=username, password=password)

        if userprofile:

            # Check if account is active
            if userprofile.is_active:

                login(request, userprofile)

                # TODO: Change http redirect to base user webspace
                return HttpResponseRedirect(reverse('basic_search:index', kwargs={'username': username})
                                            )
            else:
                # TODO: Inactive: Reutrn template ??
                return HttpResponse("Your account is disablied, please contact the system administrator")

        else:
            # Login details did not match what was in database
            print "Invalid login detials: {0}, {1}".format(username, password)

            # TODO: Create template for this??
            return HttpResponse("Invalid login details supplied")

    else:
        # nothing is in database
        return render_to_response(reverse('index:index'), {}, context)
