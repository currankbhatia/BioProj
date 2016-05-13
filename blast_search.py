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

import time

# information flow:
# 1) read input of gene id's, use Entrez to fetch the fasta files
# 2) run the output fasta file through blast to do comparisons across different species
# 3) output as xml file
# 4) parse through xml results, arrange closest matches

# questions:
# - how to do error checking on efetch paramters
# - properly parsing fasta file and paramters for qblast algorithm
# - how to parse through the xml file to extract individual species comparisons
# - use parse or read to go through xml file from blast search

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
		nucleotide = raw_input("Enter a nucleotide id ")
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

	#determine what the blast algorithm is going to search through - which data bases and which blasts
	dataset = 'blastp'
	base = 'nr'
	if(db == 'n'):
		dataset = 'blastn'
		base = 'nt'

	try:
		result_handle = NCBIWWW.qblast(dataset, base, sequence)
		save = open("my_blast.xml","w")
		save.write(result_handle.read())
		save.close()
		result_handle.close()
		return result_handle
	except:
		print "Something went wrong while trying to run the blast algorithm"
		return -1

def parseXML(nameArray):
	hand = open("my_blast.xml")
	blast_record = NCBIXML.read(hand)

	queries = open("queries.txt","w")

	E_VALUE_THRESH = 0.04

	print "Here are some results"

	d=0

	compSequences = []



	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
			if(d>=5):
				break
			if hsp.expect < E_VALUE_THRESH:
				queries.write("Alignment"+'\n')
				queries.write('sequence: ' + str(alignment.title) + '\n')
				queries.write('e value:' + str(hsp.expect) + '\n')
				queries.write(hsp.query[0:75]+ '...' + '\n')
				queries.write(hsp.sbjct[0:75]+ '...' + '\n')
				compSequences.append(hsp.sbjct)

				addStr = str(alignment.title)
				addStr += " \nalign length:"
				addStr += "{}".format(alignment.length)

				nameArray.append(addStr)

				d+=1

	queries.close()
	print compSequences[0]

	return compSequences

# main
# 1
def runcode():
	Entrez.email = "sabaimran48@gmail.com"

	print("Welcome to the tree maker! Please input a protein id that you would like to see compared across species.")

	fetched = ''
	#db = 'k'
	#valid = 0
	#while(db != 'p') and (db != 'n'):
	#	db = get_database()

	db = 'p'

	fetched = retrieve_fasta(db)

	# print sequence information
	for seq_record in SeqIO.parse(fetched,"fasta"):
		print(seq_record.id)
		print(repr(seq_record.seq))
		print(len(seq_record))
		# get the sequence
		test = Seq.Seq(str(seq_record.seq), IUPAC.unambiguous_dna)

	# my_file = open("example_fasta.fasta", "w")
	# my_file.write(str(test))

	# if returned a valid entry in the database

	if fetched != 0:
		print(fetched.read())

		print "trying blast"

		hand = blast(db,test)

		# valid blast search
		array = []

		if hand != -1:
			print "Done blasting! Parsing through results..."
			queries = parseXML(array)
			print "Here are your results"
		else:
			print "Sorry, looks like that didn't work."

	



# result_handle = NCBIWWW.qblast("blastn","nt",example_fasta)
