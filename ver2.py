
from Bio import SeqIO
for seq_record in SeqIO.parse("reston-gene-NP-Q91DE1.fasta.txt", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
