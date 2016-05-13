#! /usr/bin/python2
#Gotten from:
#http://wwwabi.snv.jussieu.fr/jompo/Public/moduleISV/Documents/GE/upgma.py
#Edited to fit in the program


theStr = []

class cluster:
    pass

def make_clusters(species):
    clusters = {}
    id = 1
    for s in species:
        c = cluster()
        c.id = id
        c.data = s
        c.size = 1
        c.height = 0
        clusters[c.id] = c
        id = id + 1
    return clusters

def find_min(clu, d):
    mini = None
    i_mini = 0
    j_mini = 0
    for i in clu:
        for j in clu:
            if j>i:
                tmp = d[j -1 ][i -1 ]
                if not mini:
                    mini = tmp
                if tmp <= mini:
                    i_mini = i
                    j_mini = j
                    mini = tmp
    return (i_mini, j_mini, mini)

def regroup(clusters, dist):
    i, j, dij = find_min(clusters, dist)
    ci = clusters[i]
    cj = clusters[j]
    # create new cluster
    k = cluster()
    k.id = max(clusters) + 1
    k.data = (ci, cj)
    k.size = ci.size + cj.size
    k.height = dij / 2.
    # remove clusters
    del clusters[i]
    del clusters[j]
    # compute new distance values and insert them
    dist.append([])
    for l in range(0, k.id -1):
        dist[k.id-1].append(0)
    for l in clusters:
        dil = dist[max(i, l) -1][min(i, l) -1]
        djl = dist[max(j, l) -1][min(j, l) -1]
        dkl = (dil * ci.size + djl * cj.size) / float (ci.size + cj.size)
        dist[k.id -1][l-1] = dkl
    # insert the new cluster
    clusters[k.id] = k

    if len(clusters) == 1:
        # we're through !
        return clusters.values()[0]
    else:
        return regroup(clusters, dist)

def pprint(tree, len, ourStr):

    if tree.size > 1:
        # it's an internal node
        print "(",
        pprint(tree.data[0], tree.height, ourStr)
        print ",",
        pprint(tree.data[1], tree.height, ourStr)
        print  ("):%2.2f" % (len - tree.height)),
    else :
        # it's a leaf
        print  ("%s:%2.2f" % (tree.data, len)),


def betterprint(tree, len):

    #print ''.join(theStr)

    if tree.size > 1:
        # it's an internal node
        theStr.append('(')
        betterprint(tree.data[0], tree.height)
        theStr.append(',')
        betterprint(tree.data[1], tree.height)
        theStr.append("):%2.2f" % (len - tree.height)),
    else :
        # it's a leaf
        theStr.append("%s:%2.2f" % (tree.data, len)),




def test():
    species = [ "A", "B", "C", "D", "E" ]
    matr = [ [ 0., 4., 5., 5., 2. ],
             [ 4., 0., 3., 5., 6. ],
             [ 5., 3., 0., 2., 5. ],
             [ 5., 5., 2., 0., 3. ],
             [ 2., 6., 5., 3., 0. ] ]
    clu = make_clusters(species)
    tree = regroup(clu, matr)
    pprint(tree, tree.height)

def mytest(): 

	
    species = [ "1", "2", "3", "4", "5" ]
    matr = [ [ 0., 1., 2., 2., 2. ],
             [ 1., 0., 2., 2., 2. ],
             [ 2, 2., 0., 1.2, 1.6 ],
             [ 2., 2., 1.2, 0., 1.6 ],
             [ 2., 2., 1.6, 1.6, 0. ] ]
    clu = make_clusters(species)
    tree = regroup(clu, matr)
    #ourStr = []

    betterprint(tree, tree.height)
    theStrString = ''.join(theStr)

    print "5 {} 6".format(theStrString)
    return theStrString

def properRun(matr, rowNum):

    species = []
    for i in range (0, rowNum):
        species.append(str(i))

    #print ''.join(species)    

    clu = make_clusters(species)
    tree = regroup(clu, matr)
    #ourStr = []

    betterprint(tree, tree.height)
    theStrString = ''.join(theStr)

    print "5 {} 6".format(theStrString)
    return theStrString




def test2():
    species = [ "Turtle", "Man", "Tuna", "Chicken",
                "Moth", "Monkey", "Dog" ]
    matr = [ [], [ 19 ], [ 27, 31 ],
             [ 8, 18, 26 ], [ 33, 36, 41, 31 ],
             [ 18, 1, 32, 17, 35 ], [ 13, 13, 29, 14, 28, 12 ] ]
    clu = make_clusters(species)
    tree = regroup(clu, matr)
    pprint(tree, tree.height)


#mytest()
