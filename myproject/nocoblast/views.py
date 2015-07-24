import ast
import os
fo = open("/home/hamza/Pictures/myproject/myblast/viewspy.txt", "a")
fo.write("Log file\n")

from Bio.Blast.Applications import NcbiblastnCommandline, NcbitblastnCommandline, NcbiblastpCommandline, NcbiblastxCommandline
from Bio.Blast import NCBIXML

from django.shortcuts import render_to_response
from django.template import RequestContext

from settings import EVALUE_BLAST_DEFAULT, BLAST_MAX_NUMBER_SEQ_IN_INPUT
from settings import EXAMPLE_FASTA_NUCL_FILE_PATH, EXAMPLE_FASTA_PROT_FILE_PATH

from forms import BlastForm, TBlastnForm
import utils


