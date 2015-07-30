from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

#added by palmer
from django.core.context_processors import csrf
from forms import MyRegistrationForm


# Create your views here.


# Main function to call the index for the main front page.


def indexview(request):
    return render(request, 'index/index.html')


def loginview(request):
    if not request.user.is_authenticated():
        return render(request, 'index/login.html')

    else:  # user is already logged in. Redirect to secure site
        # TODO: Change http redirect to base user webspace
        username = request.user.username
        return HttpResponseRedirect(reverse('secure:index', kwargs={'username': username}))


@login_required
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
                return HttpResponseRedirect(reverse('secure:index', kwargs={'username': username})
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

#added by Palmer
def doctor_register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')

    args = {}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()

    return render(request, 'index/register.html', args)

def doctor_register_success(request):
    return render_to_response('index/register_success.html')

