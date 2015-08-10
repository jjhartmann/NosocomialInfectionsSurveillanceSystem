#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ivydong
# @Date:   2015-07-26 01:33:32
# @Last Modified time: 2015-07-27 13:39:03
# Required Module: ete2 

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import sys, os, json
from pprint import pprint
from django.core.files import File
from django.conf import settings
from myproject.settings import PROJECT_ROOT
from ete2 import Tree
from django.conf.urls.static import static
import random
from django.core.context_processors import csrf
from treebuilder.models import TreebuilderFiles

# Create your views here.
newick_file = ""


def parse_outtree(request, username):
    """
    Generate json format file for dndTree.js
    """
    # path = PROJECT_ROOT + '/treebuilder/phylocanvas/example.nwk'
    # pprint("[DEBUG] open file - " + path, sys.stderr)
    # readFile = open(path, 'r')
    # content = readFile.read()
    # readFile.close()
    # pprint("[DEBUG] read file - " + content, sys.stderr)
    t = Tree(newick_file)
    jsonResult = get_json(t)
    jsonStr = repr(jsonResult).replace("'", '"')
    pprint("[DEBUG] json - " + repr(jsonStr), sys.stderr)
    writeFile = open(PROJECT_ROOT + '/graph/static/graph/flare2.json', 'w')
    writeFile.write(jsonStr)
    writeFile.close()
    return HttpResponse(jsonStr, {'username': username})


def get_json(node):
    """
    Modified from jhcepas/Newick2JSON.PY
    Converts a newick file into JSON format
    """
    # Read ETE tag for duplication or speciation events
    if not hasattr(node, 'evoltype'):
        dup = random.sample(['N', 'Y'], 1)[0]
    elif node.evoltype == "S":
        dup = "N"
    elif node.evoltype == "D":
        dup = "Y"

    node.name = node.name.replace("'", '')

    json = {"name": node.name,
            "display_label": node.name,
            "duplication": dup,
            "size": str(node.dist),
            "common_name": node.name,
            "seq_length": 0,
            "type": "node" if node.children else "leaf",
            "uniprot_name": "Unknown",
            }
    if node.children:
        json["children"] = []
        for ch in node.children:
            json["children"].append(get_json(ch))
    return json


def index(request, username, id):

    files = get_object_or_404(TreebuilderFiles, user=username)
    newick_file = files.newick_file.replace('\n', '')

    t = Tree(newick_file)
    jsonResult = get_json(t)
    jsonStr = repr(jsonResult).replace("'", '"')

    return render(request, 'graph/graph.html', {'username': username, 'parsedjson':  jsonStr})
