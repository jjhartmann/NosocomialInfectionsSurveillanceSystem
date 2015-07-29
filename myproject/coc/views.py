#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ivydong
# @Date:   2015-07-26 03:06:52
# @Last Modified time: 2015-07-27 13:40:14

from django.shortcuts import render
from django.http import HttpResponse
import sys, os , json,re
from pprint import pprint
from django.core.files import File
from django.conf import settings
from myproject.settings import PROJECT_ROOT
from django.conf.urls.static import static
import random
from collections import OrderedDict
from basic_search.models import *

# Create your views here.
def index(request,username):
	return render(request, 'coc/graph.html',{'username': username })

#genbank_accession_number = models.CharField(max_length=10, null=False, primary_key=True)
#host = models.CharField(max_length=10, null=True)
#genomesegment_or_proteinname = models.CharField(max_length=10, null=True)
#subtype = models.CharField(max_length=10, null=True)
#country = CountryField(verbose_name="Country", help_text="Origin of viral strain.", null=True)
#date_discovered = models.DateField(null=True)
#sequence_length = models.IntegerField(null=True)
#virus_name = models.CharField(max_length=30, null=True)
#age = models.FloatField(null=True)
#gender = models.CharField(max_length=2, null=True)  # change to list....
#completeness = models.CharField(max_length=2, null=True)

def parse_data(request,username):
    """
    Get input from detail search result and parse input to produce adjancency matrix
    """
    path = PROJECT_ROOT + '/coc/static/coc/matrix.json'
    pprint("[DEBUG] open file - " + path, sys.stderr)
    json_data = open(path)
    decode_data = json.load(json_data)
    x=[]
    y=[]
    group_count = 0
    for i in range (0,len(decode_data)):
        node = {"name":decode_data[i]['pk'],"group":group_count}
        incr = i+1
        x.append(node)
        str1 = decode_data[i]['pk']
        str1_group = decode_data[i]['fields']['country']
        pprint ("str1 = " + str1 , sys.stderr)
        while (incr < len(decode_data)):
            str2 = decode_data[incr]['pk']
            str2_group = decode_data[incr]['fields']['country']
            if str1_group != str2_group:
                group_count = group_count + 1
                node = {"name":decode_data[i]['pk'],"group":group_count}
            m = 0
            count = 0
            for m in range(0, len(str1)):
                if str1[m] == str2[m]:
                    count = count + 1
                if count > 0:
                    link ={'source':i,'target':incr,'value':count}
                m = m + 1
            incr = incr + 1
            y.append(link)
        parse = json.dumps({'nodes':x,'links':y}, indent = 2)
        writeFile = open(PROJECT_ROOT + '/coc/static/coc/parse.json', 'w')
        writeFile.write(parse)
        writeFile.close()
    return HttpResponse(parse,{'username': username })





