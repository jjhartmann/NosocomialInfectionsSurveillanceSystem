__author__ = 'Jeremy'

from django.core.management.base import BaseCommand, CommandError
import urllib2
import re

from basic_search.models import *


# Reverse and format the date into Django's format
def reverse_date(date_string, isfna):
    # print str
    words = date_string.split('/')
    date = ""
    if not isfna:
        if len(words) > 1:
            for i, word in enumerate(words):

                # Insure the proper format of YYYY-MM-DD
                if len(word) < 2:
                    word = "0" + word

                if (0 == i):
                    date = word
                elif (1 == i):
                    date = date + "-" + word;
                else:
                    date = word + "-" + date

        elif len(words[0]) > 1:
            if words[0] == "NON":
                date = None
            else:
                date = words[0] + "-01-01"
        else:
            date = None
    else:
        if len(words) > 1:
            date = date_string.replace('/', '-')
        elif len(words[0]) > 1:
            if words[0] == "NON":
                date = None
            else:
                date = words[0] + "-01-01"
        else:
            date = None

    # print date

    return date


# Format the age into a float value
def format_age(age_string):
    age_string_trunc = ""
    if len(age_string) != 0:
        age_string_trunc = age_string[0:len(age_string) - 1]
        return float(age_string_trunc)

    return None


# Parse and store the Influenza AA and FA data
def store_fa_aa_data(data, model, isfna):
    for line in data:
        # Split line by tab
        print "Reading Line: " + line

        splitline = re.split(r'\t', line)
        row = model(
            splitline[0],  # genbank #
            splitline[1],  # Host
            splitline[2],  # Genome sequence or protein
            splitline[3],  # subtype
            splitline[4],  # country
            reverse_date(splitline[5], isfna),  # Date
            int(splitline[6]),  # sequence length
            splitline[7],  # virus name
            format_age(splitline[8]),  # age
            splitline[9],  # gender
            splitline[10]  # completeness
        )
        row.save()


# Parse and store the FAA and FNA data
def store_fna_faa_data(data, model):
    genbank_str = ""
    genome_seq = ""
    for i, line in enumerate(data):
        print "Reading Line: " + line

        if line[0] == '>':
            # Save the data after first run
            if (i != 0):
                row = model(
                    genbank_str,
                    genome_seq,
                )
                row.save();

            splitline = re.split(r'\|', line)
            genbank_str = ""
            genome_seq = ""

            # find the genbank number
            for j, word in enumerate(splitline):
                if word == "gb":
                    genbank_str = splitline[j + 1]
                    break;

        else:
            cleanline = line.rstrip()
            genome_seq = genome_seq + cleanline

    # save the final row after iterations
    row = model(
        genbank_str,
        genome_seq,
    )
    row.save()






class Command(BaseCommand):
    help = "Refresh the database from the NCBI website"

    def writefunc(s):
        print "Read: " + s

    def handle(self, *args, **options):
        self.stdout.write('Successfully called command')

        # Get the data from NCBI
        influenzaaa = urllib2.urlopen('http://cmpt470.csil.sfu.ca:8009/~jhartman/temp_data.txt')  # for testing. ...
        influenzana = urllib2.urlopen('http://cmpt470.csil.sfu.ca:8009/~jhartman/temp_data_na.txt')  # for testing. ...
        store_fa_aa_data(influenzaaa, Influenza_AA, False)
        store_fa_aa_data(influenzana, Influenza_NA, True)

        # Get the FAA/FNA data
        influenzafaa = urllib2.urlopen('http://cmpt470.csil.sfu.ca:8009/~jhartman/temp_data_faa.txt')
        influenzafna = urllib2.urlopen('http://cmpt470.csil.sfu.ca:8009/~jhartman/temp_data_fna.txt')
        store_fna_faa_data(influenzafaa, Influenza_FAA)
        store_fna_faa_data(influenzafna, Influenza_FNA)

