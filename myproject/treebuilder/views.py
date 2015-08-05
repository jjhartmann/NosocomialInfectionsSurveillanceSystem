from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from newnoco import run_phylo
# Create your views here.

# Index view to render the main project page
@login_required
def indexview(request, username):
    return render(request, 'treebuilder/index.html', {'username': username})


@login_required
def generate(request, username):
    run_phylo()
    return render(request, 'treebuilder/phyloview1.html', {'username': username})