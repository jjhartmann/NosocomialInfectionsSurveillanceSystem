__author__ = 'Jeremy'

from django.core.management.base import BaseCommand, CommandError
import urllib2
import re
from Bio import Entrez
from Bio import SeqIO

from basic_search.models import *

# List to house the gbdata
gblist = []


# Reverse and format the date into Django's format
def reverse_date(date_string):
    # print str
    words = date_string.split('/')
    date = ""

    if len(words) == 1:
        if words[0] == "NON" or words[0] == "unknown" or (not words[0]):
            date = None
        else:
            date = words[0] + "-01-01"

    elif len(words) == 2:
        if len(words[0]) == 4 and len(words[1]) == 2:
            if int(words[1]) <= 12:
                date = date_string.replace('/', '-') + "-01"
            else:
                date = words[0] + "-01-" + words[1]
        else:
            print "ERRRRRRRRRRROOOOOOOOOOOORRRRRRRRRRRRR: Date len2"

    else:
        first = words[0]
        second = words[1]
        third = words[2]

        if len(first) == 4 and len(second) == 2 and len(third) == 2:
            if int(second) <= 12:
                date = date_string.replace('/', '-')
            else:
                date = first + "-" + third + "-" + second

        else:
            print "ERRRRRRRRRRROOOOOOOOOOOORRRRRRRRRRRRR: Date len3"

    # print date

    return date


# Format the age into a float value
def format_age(age_string):
    age_string_trunc = None
    day_test = age_string.split(" ")

    if len(day_test) > 1:
        if day_test[0].isdigit():
            day = float(day_test[0]) / 365
            return float(day)

    elif age_string == "Adult" or age_string == "-":
        return None

    elif len(age_string) > 1:
        marker = age_string[len(age_string) - 1:len(age_string)]
        agefloat = float(age_string[0:len(age_string) - 1])

        if marker.lower() == "y":
            age_string_trunc = agefloat

        elif marker.lower() == "m":
            age_string_trunc = agefloat / 12

        elif age_string.isdigit():
            return float(age_string)
        # print age_string_trunc

        return float(age_string_trunc)

    elif len(age_string) == 1 and age_string.isdigit():
        return float(age_string)

    return None


# Parse and store the Influenza AA and FA data
def store_fa_aa_data(data, model, iterations):
    gblist[:] = []
    for i, line in enumerate(data):
        # Split line by tab
        print "Reading Line: " + line
        splitline = re.split(r'\t', line)
        row = model(
            splitline[0],  # genbank #
            splitline[1],  # Host
            splitline[2],  # Genome sequence or protein
            splitline[3],  # subtype
            splitline[4],  # country
            reverse_date(splitline[5]),  # Date
            int(splitline[6]),  # sequence length
            splitline[7],  # virus name
            format_age(splitline[8]),  # age
            splitline[9],  # gender
            splitline[10]  # completeness
        )
        row.save()

        # save genbank list
        gblist.append(splitline[0])
        if (i > iterations):
            print gblist
            break;


# Parse and store the FAA and FNA data
def store_fna_faa_data(model):
    genbank_str = ""
    genome_seq = ""

    Entrez.email = "hamzakhanvit@gmail.com"
    handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=gblist)
    for i, line in enumerate(SeqIO.parse(handle, "gb")):
        genbank_str = line.id.rstrip('\n').split(".", 1)[0]
        genome_seq = line.seq.rstrip('\n')
        print "Reading Line: " + genbank_str + "   " + genome_seq
        row = model(
            genbank_str,
            genome_seq,
        )
        row.save()


class Command(BaseCommand):
    help = "Refresh the database from the NCBI website"

    def add_arguments(self, parser):
        parser.add_argument('entries', nargs=1, type=int)

    def writefunc(s):
        print "Read: " + s

    def handle(self, *args, **options):
        self.stdout.write('Successfully called command')

        iterations = 10
        if options['entries'] != 0:
            iterations = options['entries'][0]

        print iterations
        # Get the data from NCBI
        influenzana = urllib2.urlopen(
            'ftp://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/influenza_na.dat')  # for testing. ...
        store_fa_aa_data(influenzana, Influenza_NA, iterations)
        store_fna_faa_data(Influenza_FNA)

        # Get FAA data.
        influenzaaa = urllib2.urlopen(
            'ftp://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/influenza_aa.dat')  # for testing. ...
        store_fa_aa_data(influenzaaa, Influenza_AA, iterations)
        store_fna_faa_data(Influenza_FAA)



        # influenzafaa = urllib2.urlopen('ftp://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/influenza_aa.dat')
        # influenzafna = urllib2.urlopen('ftp://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/influenza.fna')



        # # Parse and store the FAA and FNA data
        # def store_fna_faa_data(data, model):
        #     genbank_str = ""
        #     genome_seq = ""
        #
        #     Entrez.email = "hamzakhanvit@gmail.com"
        #     handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=gblist)
        #     for i , line in enumerate(SeqIO.parse(handle, "gb")):
        #     # for i, line in enumerate(data):
        #         print "Reading Line: " + line
        #
        #         if line[0] == '>':
        #             # Save the data after first run
        #             if (i != 0):
        #                 row = model(
        #                     genbank_str,
        #                     genome_seq,
        #                 )
        #                 row.save();
        #
        #             splitline = re.split(r'\|', line)
        #             genbank_str = ""
        #             genome_seq = ""
        #
        #             # find the genbank number
        #             for j, word in enumerate(splitline):
        #                 if word == "gb":
        #                     genbank_str = splitline[j + 1]
        #                     break;
        #
        #         else:
        #             cleanline = line.rstrip()
        #             genome_seq = genome_seq + cleanline
        #
        #     # save the final row after iterations
        #     row = model(
        #         genbank_str,
        #         genome_seq,
        #     )
        #     row.save()
