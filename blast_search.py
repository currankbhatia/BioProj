import os
import sys
import subprocess

from Bio import Entrez
from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC
from Bio.Alphabet import Gapped, IUPAC
from Bio.Alphabet import generic_nucleotide

from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.SubsMat import FreqTable
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

# information flow:
# 1) read input of gene id's, use Entrez to fetch the fasta files
# 2) run the output fasta file through blast to do comparisons across different species
# 3) output as xml file
# 4) parse through xml results, arrange closest matches

# questions:
# - how to parse through the xml file to extract individual species comparisons

def fetch(database, ids):
	return Entrez.efetch(db = database, id=ids, rettype ="fasta")

# main
# 1
Entrez.email = "sabaimran48@gmail.com"

db = 'k'
valid = 0
while(db != 'p') and (db != 'n'):
	db = raw_input("Enter 'p' to search a protein or 'n' to search a nucleotide: ")
	# print "\n"
	if (db != 'p') and (db != 'n'):
		print("That's not a database!")
	# print(db)

if(db == 'p'):
	protein = raw_input("Enter a protein id ")
	pretend = fetch("protein", protein)
	print(pretend.read())

if(db == 'n'):
	nucleotide = raw_input("Enter a gene id for a nucleotide")
