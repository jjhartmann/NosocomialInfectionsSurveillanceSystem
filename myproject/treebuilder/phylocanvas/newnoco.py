# load the required packages
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
import os
import sys
import pylab
import matplotlib.pyplot as plt
from Bio import Phylo


# read in the input file, i.e. output of the blast result
cline = ClustalwCommandline("clustalw2", infile="fasta_temp.fa")
print(cline)
clustalw_exe = "/usr/bin/clustalw"
clustalw_cline = ClustalwCommandline(clustalw_exe, infile="fasta_temp.fa")
assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
stdout, stderr = clustalw_cline()
align = AlignIO.read("fasta_temp.aln", "clustal")
print(align)
tree = Phylo.read("fasta_temp.dnd", "newick")
# Phylo.draw_ascii(tree)
tree.rooted = True
Phylo.draw_graphviz(tree, prog="neato", node_size=0)
pylab.savefig('phylo-dot.png')
Phylo.write(tree, "example.xml", "phyloxml")
Phylo.write(tree, "example.nwk", "newick")

# tree = Phylo.read("example.xml", "phyloxml")
# Phylo.draw_graphviz(tree, prog="neato", node_size=0)
# pylab.show()
# Displays the tree in an interactive viewer
# pylab.savefig('phylo-dot.png')
