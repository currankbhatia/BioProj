#Found this example from http://biopython.org/wiki/Getting_Started
from Bio.Seq import Seq
import time

start = time.time()

#create a sequence object
my_seq = Seq('CATGTAGACTAG')

#print out some details about it
print 'seq %s is %i bases long' % (my_seq, len(my_seq))
print 'reverse complement is %s' % my_seq.reverse_complement()
print 'protein translation is %s' % my_seq.translate()

print 'find GTA %i' % my_seq.find("GTA")


print "HEOEAROGKADFGKADF:LGKADFLKGD:FGKDAF:LGKDFLGK"
print "Agdfgafdgdf"

end = time.time()

print(end-start)
