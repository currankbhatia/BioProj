
#this script goes into the xml file and prints out the 5 highest numbered hit_len genes and their gene ids

from xml.dom import minidom
import operator
from operator import itemgetter



def getHits():

	xmldoc = minidom.parse('my_blast.xml')
	itemlist = xmldoc.getElementsByTagName('Hit_len')
	itemlist2 = xmldoc.getElementsByTagName('Hit_id')
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
