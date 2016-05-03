



def printMatrix (Matrix, rowStrNum):

	for i in range(0, rowStrNum): 
	#for j in range(0, colStrNum):
		
		print Matrix[i]


def maxScore (colStr, rowStr):

	colStrNum = 1 + len(colStr)
	rowStrNum = 1 + len(rowStr)

	#print colStrNum
	#print rowStrNum

	Matrix = [[0 for x in range(colStrNum)] for y in range(rowStrNum)]



	for i in range(0, rowStrNum): 
		for j in range(0, colStrNum):
			
			Matrix[i][j] = 0

	#print Matrix


				

	match = 4
	mis = -1
	gap = -5

	# for i in range(1, rowStrNum): 
	# 	Matrix[i][0] = Matrix[i-1][0] + gap
	# for i in range(1, colStrNum):
	# 	Matrix[0][i] = Matrix[0][i-1] + gap

	# now calculate the score

	# for i in xrange(1,rowStrNum):
	# 	for j in xrange(1,colStrNum):



	#printMatrix(Matrix)


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
			



	#printMatrix(Matrix, rowStrNum)


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


	printMatrix(Matrix, len(stringArray))

	return Matrix
	
#def getSimilarity(similarityMatrix, strIdx1, strIdx2):
#	dim = len(similarityMatrix)
#	if(strIdx1 >= dim || strIdx2 >= dim) return 0
#	if(strIdx2 == strIdx1) return 0



stringArray = ["CGTGAATTCAT", "GACTTAC", "GATAGCTACTTAC", "GACCCTTTATAC", "GACTTGGGAC"]


#colStr = "CGTGAATTCAT"#"GATTACAAG"
#rowStr = "GACTTAC"#"ATTAAG"

#print maxScore(colStr, rowStr)


similarityMatrix(stringArray)





