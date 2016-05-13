# CS466 Bioinformatics Class Project 
Phylogenetic Trees via BLAST and Smith-Waterman

Installation instructions:

Install Python if needed, Install Biopython, Install Ete http://etetoolkit.org/download/

Install Biopython for anaconda: install -c anaconda biopython=1.66


Run Instructions:

Set Path by doing:
	export PATH=~/anaconda_ete/bin:$PATH

To Run: 
	python runner.py

Then simply type in gene or protein and include a the id.


conda
if not already:  install -c anaconda biopython=1.66

Some important places for reference are: 
http://www.ncbi.nlm.nih.gov/protein
http://biopython.org/DIST/docs/tutorial/Tutorial.pdf



Right now, `blast_search.py` takes in a gene id like 2388689 for the GH1 protein and we 
it runs a blast search on NCBI's database and tells us what are similar genes in the same species and other species.
Once that is complete it makes an xml file `my_blast.xml` that gives holds the similar genes, inlcluding a simlarity score, which can be used to make a matrix similarity matrix to make a phylogenetic tree. 

