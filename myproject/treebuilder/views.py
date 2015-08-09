from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from newnoco import run_phylo
from .models import TreebuilderFiles
from nocoblast.models import FASTATable


# Create your views here.

# Index view to render the main project page
@login_required
def indexview(request, username):
    return render(request, 'treebuilder/index.html', {'username': username, 'fastatable': FASTATable.objects.all(), })


@login_required
def generate(request, username, id):
    fasta = get_object_or_404(FASTATable, id=id)
    run_phylo(username, fasta)

    files = TreebuilderFiles.objects.get(user=username)
    newick = files.newick_file.replace('\n', '')
    return render(request, 'treebuilder/phyloview1.html', {'username': username, 'newick': newick, 'id': id, })

@login_required
def generate2(request, username, id):

    files = get_object_or_404(TreebuilderFiles, user=username)
    newick = files.newick_file.replace('\n', '')
    return render(request, 'treebuilder/phyloview2.html', {'username': username, 'newick': newick, 'id': id, })