from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from newnoco import run_phylo
from .models import TreebuilderFiles


# Create your views here.

# Index view to render the main project page
@login_required
def indexview(request, username):
    return render(request, 'treebuilder/index.html', {'username': username})


@login_required
def generate(request, username):
    run_phylo(username)

    files = TreebuilderFiles.objects.get(user=username)
    newick = files.newick_file.replace('\n', '')
    return render(request, 'treebuilder/phyloview1.html', {'username': username, 'newick': newick })
