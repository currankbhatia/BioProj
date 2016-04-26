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

#iteratively explores a manually inputted sequence in fasta format
for seq_rec in SeqIO.parse("oxt.fasta", "fasta"):
    print(seq_rec.id)
    print(repr(seq_rec.seq))
    print(len(seq_rec))

#creates a sequence object

oxytocin = Seq.Seq(str(seq_rec.seq), IUPAC.unambiguous_dna)

record1 = SeqRecord(oxytocin, id= "fam")
record2 = SeqRecord(oxytocin, id= "fam")

print(record1.seq == record2.seq)

my_file = open("example.fasta", "w")
my_file.write("oxt.fasta")
#print(oxytocin.translate(table=2))

#print(oxytocin)

#print(my_seq)

#finds frequency of GC pairings
alignment = AlignIO.read("oxt.fasta", "fasta")

print(str(alignment))

for record in alignment:
	print("%s - %s" % (record.seq, record.id))

print(GC(oxytocin));
print '\n';

#goes through the fasta format to look through all fasta files (helpful if scraping a database and find multiple entries under one query)
record_iterator = SeqIO.parse("oxt.fasta", "fasta")

first_record = next(record_iterator)
print(first_record.id)
print(first_record.description)
print(repr(first_record.seq))