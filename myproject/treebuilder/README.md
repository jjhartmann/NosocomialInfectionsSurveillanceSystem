for the treebuilder Phyapp, we need the following:
1. Biopython installation: sudo apt-get install python-biopython
2. Networkx: sudo pip install networkx
3. Matplotlib: sudo apt-get install python-matplotlib
4. Clustalw: sudo apt-get install clustalw
5. Pygraphwiz: sudo apt-get install pygraphviz
6. Pydot: sudo apt-get install python-pydot

Things critical:
1. Retrieve the fasta file, generated in the BLAST results located at: myproject/nocoblast/fasta_temp.fa (would stil confirm this)
2. simple template created, which should run the python script nocophylo.py in the background onclick of the button.
3. The results should be displayed using the js script in the phylocanvas folder (myproject/treebuilder/phylocanvas/PhyloCanvas.js)

