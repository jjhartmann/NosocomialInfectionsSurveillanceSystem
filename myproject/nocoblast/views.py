import ast
import os, json
#fo = open("/home/hamza/Pictures/myproject/nocoblast/viewspy.txt", "a")
#fo.write("Log file\n")

from Bio.Blast.Applications import NcbiblastnCommandline, NcbitblastnCommandline, NcbiblastpCommandline, NcbiblastxCommandline
from Bio.Blast import NCBIXML
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template import RequestContext

from settings import EVALUE_BLAST_DEFAULT, BLAST_MAX_NUMBER_SEQ_IN_INPUT
from settings import EXAMPLE_FASTA_NUCL_FILE_PATH, EXAMPLE_FASTA_PROT_FILE_PATH

from forms import BlastForm, TBlastnForm
import utils

@login_required
def blast(request, username, blast_form, template_init, template_result, blast_commandline, sample_fasta_path, extra_context=None):
    """
    Process blastn/tblastn (blast+) query or set up initial blast form.
    """

    if request.method == 'POST':

        form = blast_form(request.POST)

        if form.is_valid():

            query_file_object_tmp = form.cleaned_data['sequence_in_form']
            evalue = float(form.cleaned_data['evalue_in_form'])
            word_size = int(form.cleaned_data['word_size_in_form'])
            database_path = str(form.cleaned_data['blast_nucl_in_form'])

            standard_opt_dic = {'query': query_file_object_tmp, 'evalue': evalue, 'outfmt': 5, 'db': database_path, 'word_size': word_size}

            # none standard options:
            try:
                matrix = str(form.cleaned_data['matrix_in_form'])
                standard_opt_dic["matrix"] = matrix
            except:
                pass

            sensitivity_opt_dic = ast.literal_eval(str(form.cleaned_data['search_sensitivity_in_form']))

            # standard_opt_dic = {'query': query_file_object_tmp, 'evalue': evalue, 'outfmt': 5, 'db': nocoblast_db, "matrix": matrix, 'word_size': word_size}

            blast_records__file_xml = None
            try:
                """
                blast search, parse results from temp file, put them into template for rendering.
                """
                #fo.write(str(blast_commandline))
                blast_records__file_xml, blast_error = utils.run_blast_commands(blast_commandline, **dict(standard_opt_dic, **sensitivity_opt_dic))
                
                if len(blast_error) > 0:
                    return render_to_response(template_result, {"blast_record": ''}, context_instance=RequestContext(request))

                else:
                    blast_records = NCBIXML.parse(blast_records__file_xml)
                    #print json.dumps((blast_records__file_xml.name),sort_keys=True, indent=4)
                    #print blast_records__file_xml.name
                    # converts blast results into objects and pack into list
                    blast_records_in_object_and_list = utils.blast_records_to_object(list(blast_records))
                    
#Function for blast record vars for JSON
                    class myjsonrecord:
 
                        def __init__(self,contig,query,length,evalue,score,indent):
 
                             self.contig=contig
                             self.query=query
                             self.length=length
                             self.evalue=evalue
                             self.score=score
                             self.indent=indent

#Function for alignment vars for JSON
                    class myjsonalign:
 
                        def __init__(self,length,evalue,score,indent,positives,bits,query_start,query_end,subject_start,subject_end):
 
                             self.length=length
                             self.evalue=evalue
                             self.score=score
                             self.indentities=indent
                             self.positives=positives
                             self.bits=bits
                             self.query_start=query_start
                             self.query_end=query_end
                             self.subject_start=subject_start
                             self.subject_end=subject_end


#JSON Parser for blast output
                    
                    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
                    json_temp = os.path.join(THIS_DIR, 'my-output.json')
                    with open(json_temp, 'w') as f:
                       f.write("{ \"Description\": [")
                       for br in blast_records_in_object_and_list:
                             for alignment in br.alignments:
                                         myrecord=myjsonrecord(str(alignment.get_id()),str(br.query),str(alignment.length),str(alignment.best_evalue()),str(alignment.get_id()), str(alignment.best_identities()))
                                         #print vars(myrecord)
                                         f.write(json.dumps(vars(myrecord))) 
                                         f.write(",")
                       f.seek(-1, os.SEEK_END)
                       f.truncate()
                       f.write("], \n\"Alignments\": [{")
                       
                       for br in blast_records_in_object_and_list:
                             for alignment in br.alignments:
                                 f.write("\"%s\":[" % (alignment.hit_def))
                                 for hsp in alignment.hsp_list:
                                         myalign=myjsonalign(str(hsp.align_length),str(hsp.expect),str(hsp.score),str(hsp.identities), str(hsp.positives), str(hsp.bits), str(hsp.query_start), str(hsp.query_end),str(hsp.sbjct_start), str(hsp.sbjct_end))                
                                         #print vars(myalign)
                                         f.write(json.dumps(vars(myalign))) 
                                         f.write(",")
                                 f.seek(-1, os.SEEK_END)
                                 f.truncate()
                                 f.write("],")
                             f.seek(-1, os.SEEK_END)
                             f.truncate()
                       f.write("}]}")

                    try:
                        '''
                        user defined function to modify blast results
                        e.g. join blast results with external database in template

                        '''
                        if extra_context is not None:
                            blast_records_in_object_and_list = extra_context(blast_records_in_object_and_list)
                    except:
                        pass

                    return render_to_response(template_result,
                                              {'application': blast_records_in_object_and_list[0].application,
                                               'version': blast_records_in_object_and_list[0].version,
                                               'blast_records': blast_records_in_object_and_list,
                                               'username': username, },
                                              context_instance=RequestContext(request))

            finally:
                # remove result - temporary file
                if blast_records__file_xml is not None:
                    os.remove(blast_records__file_xml.name)

    else:
        form = blast_form(initial={'sequence_in_form': '', 'evalue_in_form': EVALUE_BLAST_DEFAULT})

    return render_to_response(template_init, {'form': form, 'sequence_sample_in_fasta': utils.get_sample_data(sample_fasta_path),
                                              "blast_max_number_seq_in_input": BLAST_MAX_NUMBER_SEQ_IN_INPUT,
                                              'username': username,
                                              }, context_instance=RequestContext(request))

@login_required
def tblastn(request, username, blast_form=TBlastnForm, template_init='nocoblast/blast.html', template_result='nocoblast/blast_results.html', extra_context=None):
    return blast(request, username=username, blast_form=blast_form, template_init=template_init, template_result=template_result, blast_commandline=NcbitblastnCommandline,
                 sample_fasta_path=EXAMPLE_FASTA_PROT_FILE_PATH, extra_context=extra_context)

@login_required
def blastn(request, username, blast_form=BlastForm, template_init='nocoblast/blast.html', template_result='nocoblast/blast_results.html', extra_context=None):
    return blast(request, username=username, blast_form=blast_form, template_init=template_init, template_result=template_result, blast_commandline=NcbiblastnCommandline,
                 sample_fasta_path=EXAMPLE_FASTA_NUCL_FILE_PATH, extra_context=extra_context)
