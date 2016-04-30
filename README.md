# CS466 Class Project
Bioinformatics Class Project

Some important places for reference are: 
http://geneontology.org/
http://www.ncbi.nlm.nih.gov/gene
http://biopython.org/DIST/docs/tutorial/Tutorial.pdf

http://rosalind.info/problems/frmt/


Right now, `blast_search.py` takes in a gene id like 2388689 for the GH1 protein and we 
it runs a blast search on NCBI's database and tells us what are similar genes in the same species and other species.
Once that is complete it makes an xml file `my_blast.xml` that gives holds the similar genes, inlcluding a simlarity score,
which can be used to make a matrix similarity matrix to make a phylogenetic tree. 

