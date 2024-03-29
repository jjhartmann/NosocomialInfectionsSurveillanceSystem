"""Module with utility functions for nocoblast app.   """
import StringIO

import tempfile
import re
import os
from Bio.Application import ApplicationError
from Bio import Entrez
from Bio import SeqIO
from features.record import Alignment, BlastRecord, Hsp
from nocoblast.models import FASTATable

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_sample_data(sample_file):
    """Read and returns sample data to fill form with default sample sequence.  """

    sequence_sample_in_fasta = None
    with open(sample_file) as handle:
        sequence_sample_in_fasta = handle.read()

    return sequence_sample_in_fasta


def fetch_entrez_seq(id_list):
    fasta_temp = os.path.join(THIS_DIR, 'fasta_temp.fa')
    os.system("rm 'fasta_temp'")
    fo = open(fasta_temp, "w")
    Entrez.email = "hamzakhanvit@gmail.com"
    handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=id_list)

    fasta_str = StringIO.StringIO()

    for seq_record in SeqIO.parse(handle, "gb"):
        fasta_str.write(">%s,%s\n%s\n" % ((seq_record.id.rstrip('\n')),seq_record.description,(seq_record.seq.rstrip('\n'))))
        # fo.write(">%s,%s\n%s\n" % ((seq_record.id.rstrip('\n')),seq_record.description,(seq_record.seq.rstrip('\n'))))

    # Store in db
    print("\nID LIST IN BLAST\n")
    print(id_list)

    try:
        id = FASTATable.objects.get(desc=id_list)
    except (FASTATable.DoesNotExist):
        row = FASTATable(desc=id_list, fasta=fasta_str.getvalue())
        row.save()



def blast_records_to_object(blast_records):
    """Transforms biopython's blast record into blast object defined in django-nocoblast app.  """

    # container for transformed objects
    blast_objects_list = []
    id_list = ""
    for blast_record in blast_records:
        counter = 0
        br = BlastRecord(**{'query': blast_record.query,
                            'version': blast_record.version,
                            'expect': blast_record.expect,
                            'application': blast_record.application,
                            'reference': blast_record.reference})
        
        #fo = open(os.path.join(THIS_DIR, 'test'), "a")
        for alignment in blast_record.alignments:
            counter+=1;
            al = Alignment(**{
                'hit_def': alignment.hit_def,
                'title': alignment.title,
                'length': alignment.length,
            })
            if(counter<10):
                  pattern = '^gi\|(.*?)\|'
                  matchObj = re.match( pattern,(str(alignment.title)))
                  matchObj = str(matchObj.group(0))[3:-1]
                  #matchObj = fo.write("%s," % (matchObj))
                  id_list += matchObj + ","
                  #fo.write(str(id_list))
        
            for hsp in alignment.hsps:
                h = Hsp(**{
                    'align_length': hsp.align_length,
                    'bits': hsp.bits,
                    'expect': hsp.expect,
                    'frame': hsp.frame,
                    'gaps': hsp.gaps,
                    'identities': hsp.identities,
                    'match': hsp.match,
                    'num_alignments': hsp.num_alignments,
                    'positives': hsp.positives,
                    'query': hsp.query,
                    'query_end': hsp.query_end,
                    'query_start': hsp.query_start,
                    'sbjct': hsp.sbjct,
                    'sbjct_end': hsp.sbjct_end,
                    'sbjct_start': hsp.sbjct_start,
                    'score': hsp.score,
                    'strand': hsp.strand,
                    'str': str(hsp),
                })

                al.hsp_list.append(h)
            br.alignments.append(al)
        blast_objects_list.append(br)
        #fo.write(str(id_list))
        fetch_entrez_seq(id_list);
    return blast_objects_list


def run_blast_commands(ncbicommandline_method, **keywords):
    """Runs nocoblast/tblastn search, collects result and pass as a xml temporary file.  """
    #fo.write(str(ncbicommandline_method))
    # temporary files for output
    blast_out_tmp = tempfile.NamedTemporaryFile(delete=False)
    blast_out_tmp_str = StringIO.StringIO()

    # keywords['out'] = blast_out_tmp_str
    keywords['out'] = blast_out_tmp.name

    # unpack query temp file object
    query_file_object_tmp = keywords['query']
    keywords['query'] = query_file_object_tmp.name

    stderr = ''
    error_string = ''
    try:
        # formating nocoblast command
        nocoblastx_cline = ncbicommandline_method(**keywords)
        print(str(nocoblastx_cline))
        stdout, stderr = nocoblastx_cline()

    except ApplicationError as e:
        error_string = "Runtime error: " + stderr + "\n" + e.cmd

    # remove query temp file
    blastxml = os.path.join(THIS_DIR, 'recent_blast.xml')
    blastjson = os.path.join(THIS_DIR, 'blast.json')
    cmd = "cp %s %s"%(blast_out_tmp.name, blastxml)
    print cmd
    os.system(cmd)
    cmd = "xml2json --input %s --output %s" %(blastxml, blastjson)
    os.system(cmd)
    os.remove(query_file_object_tmp.name)

    return blast_out_tmp, error_string
