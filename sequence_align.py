
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


from ete3 import Tree, TreeStyle
#from ete2.treeview import drawer
# remember to activate Anaconda before using ete
#with : export PATH=~/anaconda_ete/bin:$PATH
from upgma import properRun

from blast_search import parseXML

def printMatrix (Matrix, rowStrNum):

	for i in range(0, rowStrNum): 
	#for j in range(0, colStrNum):
		
		print Matrix[i]


def maxScore (colStr, rowStr):

	colStrNum = 1 + len(colStr)
	rowStrNum = 1 + len(rowStr)

	Matrix = [[0 for x in range(colStrNum)] for y in range(rowStrNum)]

	for i in range(0, rowStrNum): 
		for j in range(0, colStrNum):
			
			Matrix[i][j] = 0

	match = 4
	mis = -1
	gap = -5

	for i in range(1, rowStrNum): #vertical 
		for j in range(1, colStrNum): #horizontal

			matcher = 0

			if (rowStr[i-1] == colStr[j-1]):
				matcher = match
			else:
				matcher = mis

			scoreUp = Matrix[i-1][j] + gap
			scoreLeft = Matrix[i][j-1] + gap 
			scoreDiag = Matrix[i-1][j-1] + matcher

			maxer = max(scoreUp, scoreLeft)
			maxerFinal = max(maxer, scoreDiag)

			Matrix[i][j] = maxerFinal
	maxScore = 0

	for i in range(0, rowStrNum): 
		for j in range(0, colStrNum):

			if (Matrix[i][j] > maxScore):
				maxScore = Matrix[i][j]
	#print maxScore
	return maxScore


def similarityMatrix(stringArray):
	Matrix = [[0 for x in range(len(stringArray))] for y in range(len(stringArray))]

	for i in range(0, len(stringArray)): 
			for j in range(i+1, len(stringArray)):

				Matrix[i][j] = maxScore(stringArray[i], stringArray[j])


	#printMatrix(Matrix, len(stringArray))

	return Matrix
	
def getSimilarity(similarityMatrix, strIdx1, strIdx2):
        dim = len(similarityMatrix[0])
        if(strIdx1 >= dim | strIdx2 >= dim): return 0
        if(strIdx2 == strIdx1): return 0
        if(strIdx2 < strIdx1):
            temp = strIdx1
            strIdx1 = strIdx2
            strIdx2 = temp
        return - similarityMatrix[strIdx1][strIdx2]



def runcode():

	stringArray = ["CGTGAATTCAT", "GACTTAC", "GATAGCTACTTAC", "GACCCTTTATAC", "GACTTGGGAC"]

	sM = similarityMatrix(stringArray)

	score = getSimilarity( sM , 2, 3)
	#matrix2CSV( sM, "similarityMatrix.csv")

	print score


	#t = Tree( "((a,b),c);" )
	#t = Tree("(Bovine:0.69395,(Gibbon:0.36079,(Orang:0.33636,(Gorilla:0.17147,(Chimp:0.19268, Human:0.11927):0.08386):0.06124):0.15057):0.54939,Mouse:1.21460):0.10;")
	ourStr = mytest()
	ourStr += ";"
	
	t = Tree(ourStr)
	ts = TreeStyle()
	ts.show_leaf_name = True
	ts.show_branch_length = True
	#ts.show_branch_support = True
	t.show(tree_style=ts)

	#t.show()

def wholeMat(mat):

	for i in range(0, len(mat)): 
			for j in range(i+1, len(mat)):

				mat[j][i] = mat[i][j]

	return mat

def invertNumMat(mat): 


	#find largest number
	maxScore = 0

	for i in range(0, len(mat)): 
		for j in range(0, len(mat)):

			if (mat[i][j] > maxScore):
				maxScore = mat[i][j]

	# take largest number and subtract diff and multiply by 2 and add it the number
	for i in range(0, len(mat)): 
		for j in range(0, len(mat)):

			if not mat[i][j] == 0 or mat[i][j] == maxScore:
				# do nothing 
				#do nothing
			
				diff = maxScore - mat[i][j]
				mat[i][j] += (2*diff)



	return mat


def actualRun():

	#stringArray = ["CGTGAATTCAT", "GACTTAC", "GATAGCTACTTAC", "GACCCTTTATAC", "GACTTGGGAC"]
	stringArray = parseXML()

	sM = similarityMatrix(stringArray)
	printMatrix(sM, len(stringArray))
	fullMat = wholeMat(sM)
	printMatrix(fullMat, len(stringArray))
	score = getSimilarity( sM , 2, 3)
	print score

	mat = invertNumMat(fullMat)
	printMatrix(mat, len(stringArray))

	items = len(stringArray)

	print items

	ourStr = properRun(mat, items)
	ourStr += ";"
	
	t = Tree(ourStr)
	ts = TreeStyle()
	ts.show_leaf_name = True
	ts.show_branch_length = True
	#ts.show_branch_support = True
	t.show(tree_style=ts)

	#t.show()



#mat = [[0,1,2,2,2], [1,0,2,2,2], [2, 2, 0, 1.2, 1.6], [2, 2, 1.2, 0, 1.6], [2, 2, 1.6, 1.6, 0]]
#printMatrix(mat, 5)
#print matrixToNewick(mat)


actualRun()



