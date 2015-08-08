from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

#added by palmer
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from collections import Counter
from basic_search.models import *
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

def data_graph_json(request):
    #pip install Counter
  import json, os
  
  a = Influenza_NA.objects.all()
  countries=[]
  #for i in a:
   #  b = i.__dict__
    # countries.append(b['country'])
     #countries = list(set(countries))
  #print countries

  for i in a:
     b = i.__dict__
     print b
     countries.append(b['country'])
     #print b['country']

  myDict = Counter(countries);
  myDict    
  #for key in myDict:
    #print key
    #print myDict[key]
  THIS_DIR = os.path.dirname(os.path.abspath(__file__))
  data_jsonfile = os.path.join(THIS_DIR, '../static/data/data.json')
  with open(data_jsonfile, 'w') as fp:  
   fp.write("[\n")
   for key in myDict:
    print key
    sw=0
    av=0
    hu=0
    for i in a:
       b = i.__dict__  
       if(b['country']==key) and (b['host']=='Swine'):
                 sw+=1
       if(b['country']==key) and (b['host']=='Human'):
                 hu+=1
       if(b['country']==key) and (b['host']=='Avian'):
                 av+=1
    print sw, "\n"
    print av, "\n"
    print hu, "\n"  
    fp.write(("{\"Country\":\"").rstrip('\n'))
    fp.write((key).rstrip('\n'))
    fp.write((("\",\"freq\":{\"human\":%s,\"avian\":%s,\"swine\":%s}},") % (hu,av,sw)) .rstrip('\n'))
    fp.write("\n")     
    #print myDict[key]
   fp.seek(-2, os.SEEK_END)
   fp.truncate()
   fp.write("]")
  return render_to_response('index/chart2.html')

#Project descritpion page
def project_des(request):
  return render_to_response('index/project_des.html')

#blast introduction page
def blast(request):
  return render_to_response('index/blast.html')

#phylib introduction page
def phylib_intro(request):
  return render_to_response('index/phylib_intro.html')

#symtoms introduction page
def symptoms(request):
  return render_to_response('index/symptoms.html')

#causes introduction page
def cause(request):
  return render_to_response('index/cause.html')