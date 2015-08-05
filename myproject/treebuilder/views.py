from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

# Index view to render the main project page
@login_required
def indexview(request, username):
    return render(request, 'treebuilder/index.html', {'username': username})
