import os
import sys
import subprocess
import urllib2

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
# - how to do error checking on efetch paramters
# - properly parsing fasta file and paramters for qblast algorithm
# - how to parse through the xml file to extract individual species comparisons

def fetch(database, ids):
	return Entrez.efetch(db = database, id=ids, rettype ="fasta")

def retrieve_fasta(db):
	if(db == 'p'):
		protein = raw_input("Enter a protein id ")
		try:
			fetched = fetch("protein", protein)
			return fetched
		except urllib2.HTTPError, error:
			print "That's an invalid input, dummy"
			return 0

	if(db == 'n'):
		nucleotide = raw_input("Enter a gene id for a nucleotide")
		try:
			fetched = fetch("nucleotide", nucleotide)
			return fetched
		except urllib2.HTTPError, error:
			print "That's an invalid input, dummy"
			return 0

def get_database():
	db = raw_input("Enter 'p' to search a protein or 'n' to search a nucleotide: ")
	# print "\n"
	if (db != 'p') and (db != 'n'):
		print("That's not a database!")
	# print(db)
	else:
		return db

def blast(db, sequence):

	print('Doing the BLAST and retrieving the results...')
	# only need to input the pure sequence, but how to determine which databases to compare against?
	try:
		result_handle = NCBIWWW.qblast('blastp', 'nr', test)
		save = open("my_blast.xml","w")
		save.write(hand.read())
		save.close()
		hand.close()
		return result_handle
	except:
		print "oops"

# main
# 1
Entrez.email = "sabaimran48@gmail.com"

print("Welcome to the tree maker! Please input a gene id that you would like to see compared across species.")

fetched = ''
db = 'k'
valid = 0
while(db != 'p') and (db != 'n'):
	db = get_database()

fetched = retrieve_fasta(db)

for seq_record in SeqIO.parse(fetched,"fasta"):
	print(seq_record.id)
	print(repr(seq_record.seq))
	print(len(seq_record))
	test = Seq.Seq(str(seq_record.seq), IUPAC.unambiguous_dna)

# my_file = open("example_fasta.fasta", "w")
# my_file.write(str(test))

# if returned a valid entry in the database
if fetched != 0:
	print(fetched.read())

	
	hand = blast(db,test)

	print "done blasting"

# result_handle = NCBIWWW.qblast("blastn","nt",example_fasta)
