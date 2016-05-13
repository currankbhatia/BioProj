
from blast_search import runcode
from sequence_align import actualRun
import time

start = time.time()
runcode()
end = time.time()

print "time: {}".format(end - start)

actualRun()
