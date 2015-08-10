# load the required packages
import StringIO
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import os
import sys
# import pylab
import matplotlib.pyplot as plt
from Bio import Phylo
import platform
import tempfile
from .models import TreebuilderFiles


def run_phylo(user, fasta):
    # read in the input file, i.e. output of the blast result
    fasta_temp = os.path.abspath("./treebuilder/phylocanvas/fasta_temp.fa")
    fasta_aln = os.path.abspath("./treebuilder/phylocanvas/fasta_temp.aln")
    fasta_dnd = os.path.abspath("./treebuilder/phylocanvas/fasta_temp.dnd")
    phylo_dot = os.path.abspath("./treebuilder/phylocanvas/phylo-dot.png")
    example_xml = os.path.abspath("./treebuilder/phylocanvas/example.xml")
    example_nwk = os.path.abspath("./treebuilder/phylocanvas/example.nwk")

    fasta_temp_file = tempfile.NamedTemporaryFile()
    fasta_temp_file.write(fasta.fasta)

    cline = ClustalwCommandline("clustalw2", infile=fasta_temp_file.name)
    print(cline)

    if platform.system() == 'Windows':
        clustalw_exe = "C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    else:
        clustalw_exe = "/usr/bin/clustalw"

    clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fasta_temp_file.name)
    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
    stdout, stderr = clustalw_cline()

    align = AlignIO.read(fasta_temp_file.name + ".aln", "clustal")

    print(align)
    tree = Phylo.read(fasta_temp_file.name + ".dnd", "newick")

    # Phylo.draw_ascii(tree)
    tree.rooted = True
    # Phylo.draw_graphviz(tree, prog="neato", node_size=0)

    # pylab.savefig(phylo_dot)

    nwk = StringIO.StringIO()
    xml = StringIO.StringIO()

    Phylo.write(tree, xml, "phyloxml")
    Phylo.write(tree, nwk, "newick")

    # TODO: Decide if we want to store more dynamic content under the user.
    row = TreebuilderFiles(user=user, newick_file=nwk.getvalue(), phyloxml_file=xml.getvalue())
    row.save()

    # Clean up temp files.
    os.remove(fasta_temp_file.name + ".aln")
    os.remove(fasta_temp_file.name + ".dnd")
