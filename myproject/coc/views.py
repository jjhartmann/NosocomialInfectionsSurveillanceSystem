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

def parse_data(request,username):
    """
    Get input from detail search result and parse input to produce adjancency matrix
    """
    if request.method == 'POST':
        display = request.POST.getlist('displays')
    # pprint("[DEBUG] get checkbox value - " + repr(display), sys.stderr)
    for dis in display:
        pprint("[DEBUG] get checkbox value - " + repr(dis), sys.stderr)
    # Define path to open input file
    path = PROJECT_ROOT + '/coc/static/coc/matrix.json'
    pprint("[DEBUG] open file - " + path, sys.stderr)
    # Define a variable to contain input
    json_data = open(path)
    # Decode json format to python object (key:value) pairs
    decode_data_total = json.load(json_data)
    decode_data = []
    # Store the user selected rows in decode_data[]
    for i in range(0, len(decode_data_total)):
        for j in range (0, len(display)):
            if display[j] == decode_data_total[i]['pk']:
                decode_data.append(decode_data_total[i])
    # Create an array to store node and link
    node = []
    link = []
    # Create an array to store country, host, date and sequence
    countries=[]
    hosts = []
    dates = []
    sequences = []
    total_node = len(decode_data)

    for i in range (0, total_node):
        dates.append(decode_data[i]['fields']['date_discovered'])
        sequences.append(decode_data[i]['fields']['sequence_length'])
    # Sort the date and sequence then prepare data
    dates.sort()
    sequences.sort()
    # Use the for loop to re-index the element
    for i in range (0, total_node):
        # Declare a variable to keep track of index
        country_index = -1;
        # Initialize same indicator as 0, which means it is false
        same = 0
        for item in countries:
            if item == decode_data[i]['fields']['country']:
                # if the item in decode_data is already in the country list, assign same to 1
                same = 1
        if same == 0:
            countries.append(decode_data[i]['fields']['country'])

        country_index = countries.index(decode_data[i]['fields']['country'])
        pprint ("country index = " + repr(country_index), sys.stderr)
        host_index = -1;
        same_2 = 0
        for item in hosts:
            if item == decode_data[i]['fields']['host']:
                # if the item in decode_data is already in the host list, assign same to 1
                same_2 = 1
        if same_2 == 0:
            hosts.append(decode_data[i]['fields']['host'])
        host_index = hosts.index(decode_data[i]['fields']['host'])

        dates.append(decode_data[i]['fields']['date_discovered'])
        sequences.append(decode_data[i]['fields']['sequence_length'])

        incr = i+1
        str1 = decode_data[i]['pk']

        pprint ("str1 = " + str1 , sys.stderr)
        while (incr < total_node):
            str2 = decode_data[incr]['pk']
            m = 0
            count = 0

            # Compare each element in string 1 and string 2, increment count if character is same
            for m in range(0, len(str1)):

                for n in range(0,len(str2)):
                    if str2[n] == str1[m]:
                        count = count + 1
            # Create a link between two elements if their names have same ch
            if count > 0:
                link.append({'source':i,'target':incr,'value':count})
            incr = incr + 1
        # date and sequence block
        date_index = dates.index(decode_data[i]['fields']['date_discovered'])
        pprint ("sort index = " + repr(date_index), sys.stderr)
        sequence_index = sequences.index(decode_data[i]['fields']['sequence_length'])
        node.append({"name":decode_data[i]['pk'],"group":country_index,"host": host_index, "date": date_index, "sequences": sequence_index})
    # After the for loop is done, write into json file
    parse = json.dumps({'nodes':node,'links':link}, indent = 2)
    writeFile = open(PROJECT_ROOT + '/coc/static/coc/parse.json', 'w')
    writeFile.write(parse)
    writeFile.close()
    return render(request, 'coc/graph.html',{'username': username })





