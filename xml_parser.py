
#this script goes into the xml file and prints out the 5 highest numbered hit_len genes and their gene ids

from xml.dom import minidom
import operator
from operator import itemgetter

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


def getHits():

	xmldoc = minidom.parse('my_blast.xml')
	itemlist = xmldoc.getElementsByTagName('Hit_len')
	itemlist2 = xmldoc.getElementsByTagName('Hit_accession')
	#print(len(itemlist))
	#print(itemlist[0].attributes['name'].value)
	retlist = []
	i = 0
	for s in itemlist:
		#print("%d : %s " % (i,s.childNodes[0].nodeValue))
		stuff = {'id': itemlist2[i].childNodes[0].nodeValue, 'len': int(s.childNodes[0].nodeValue)}
		retlist.append(stuff)
		#print(stuff)
		i += 1


	return retlist

def top5(mylist):
	max = -1
	#sortedlist = sorted(mylist['len'], reverse=True)
	#sortedlist =  mylist.sort(key=operator.itemgetter('len'))
	sortedlist = sorted(mylist, key=itemgetter('len'), reverse=True)

	j = 0
	retlist = []
	for s in sortedlist:	
		#print("%d : %s " % (j,s))
		retlist.append(s)
		if j == 4:
			break
		j += 1	
	
	
	return retlist


mylist  = getHits()
final5 = top5(mylist)

for y in final5:
	print(y)

Entrez.email = "currankbhatia@gmail.com"

seqList = []

for f in final5:
	fetched = ''
	database = "protein"
	ids = ''
	ids = f.get('id') 
	fetched = Entrez.efetch(db = database, id=ids, rettype ="fasta")



	for seq_record in SeqIO.parse(fetched,"fasta"):
		print(seq_record.id)
		print(repr(seq_record.seq))
		print(len(seq_record))
		# get the sequence
		seqList.append(Seq.Seq(str(seq_record.seq), IUPAC.unambiguous_dna))


#for t in seqList:
#	print(t)
	



