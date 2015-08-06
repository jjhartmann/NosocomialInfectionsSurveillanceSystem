# load the required packages
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import os
import sys
import pylab
import matplotlib.pyplot as plt
from Bio import Phylo
import platform


def run_phylo():
    # read in the input file, i.e. output of the blast result
    fasta_temp = os.path.abspath("./treebuilder/phylocanvas/fasta_temp.fa")
    fasta_aln = os.path.abspath("./treebuilder/phylocanvas/fasta_temp.aln")
    fasta_dnd = os.path.abspath("./treebuilder/phylocanvas/fasta_temp.dnd")
    phylo_dot = os.path.abspath("./treebuilder/phylocanvas/phylo-dot.png")
    example_xml = os.path.abspath("./treebuilder/phylocanvas/example.xml")
    example_nwk = os.path.abspath("./treebuilder/phylocanvas/example.nwk")

    cline = ClustalwCommandline("clustalw2", infile=fasta_temp)
    print(cline)

    if platform.system() == 'Windows':
        clustalw_exe = "C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    else:
        clustalw_exe = "/usr/bin/clustalw"

    clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fasta_temp)
    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
    stdout, stderr = clustalw_cline()

    align = AlignIO.read(fasta_aln, "clustal")
    # align = AlignIO.read("./phylocanvas/fasta_temp.aln", "clustal")

    print(align)
    tree = Phylo.read(fasta_dnd, "newick")
    # tree = Phylo.read("./phylocanvas/fasta_temp.dnd", "newick")

    # Phylo.draw_ascii(tree)
    tree.rooted = True
    Phylo.draw_graphviz(tree, prog="neato", node_size=0)

    pylab.savefig(phylo_dot)
    # pylab.savefig('./phylocanvas/phylo-dot.png')

    Phylo.write(tree, example_xml, "phyloxml")
    # Phylo.write(tree, "./phylocanvas/example.xml", "phyloxml")

    Phylo.write(tree, example_nwk, "newick")
    # Phylo.write(tree, "./phylocanvas/example.nwk", "newick")

    # tree = Phylo.read("example.xml", "phyloxml")
    # Phylo.draw_graphviz(tree, prog="neato", node_size=0)
    # pylab.show()
    # Displays the tree in an interactive viewer
    # pylab.savefig('phylo-dot.png')
