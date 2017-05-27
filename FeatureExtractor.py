class Graph():
    def __init__(self):
        self.G = {}

    def addNode(self, node):
        if node not in self.G:
            self.G[node] = []

    def addEdge(self, node1, node2):
        if not node1 == node2:
            self.addNode(node1)
            self.addNode(node2)
            self.G[node1].append(node2)

    def neighboorhoodOverlap(self,node1,node2):
        if not ( node1 in self.G and node2 in self.G):
            return 0
        list1 = set(self.G[node1])
        list2 = set(self.G[node2])
        listIntersect = list1.intersection(list2)
        listUnion = list1.union(list2)
        if len(listUnion)==0:
            return 0
        return 1.0*len(listIntersect) / len(listUnion)

    def getDict(self):
        return self.G


def makeGML(filename,dict):

    filehandler = open(filename,"w")

    nodeNames =[]
    for key in dict:
        nodeNames.append(key)
        for name in dict[key]:
            nodeNames.append(name)
    nodeNames = list(set(nodeNames))


    filehandler.write("graph\n[\n")
    for name in nodeNames:
        filehandler.write('\tnode\n\t[\n\t\tid '+name+'\n \t\tlabel "'+name+'"\n\t]\n')

    for target in dict:
        #dict[target] = list(set(dict[target]))
        dict[target].sort()
        for source in dict[target]:
                filehandler.write('\tedge\n\t[\n\t\tsource "'+source+'"\n \t\ttarget "'+target+'"\n\t]\n')
    filehandler.write("]")
    filehandler.close()

'''
graph= Graph()
train = open("training_set.txt","r").read().split("\n")
connected = []
not_connected = []
for example in train:
    n1, n2, s = example.split(" ")
    if int(s)==1:
        graph.addEdge(n1,n2)

for example in train:
    n1,n2,s = example.split(" ")
    if int(s)==1:
        connected.append(graph.neighboorhoodOverlap(n1,n2))
    else:
        not_connected.append(graph.neighboorhoodOverlap(n1,n2))
'''


def prepareInformationMap(filename):
   map = {}
   rawData =  open(filename,"r").read().split("\n")[:-1]
   for line in rawData:
       features = line.split(",")
       print(features)
       map[features[0]] = features[1:]
   return map

def extractEdgeFeatures(nodeInformationMap,node1,node2):
    infoNode1 = nodeInformationMap[node1]
    infoNode2 = nodeInformationMap[node2]
    yearsDifference = abs( int(infoNode1[0]) - int(infoNode2[0]))


def buildDictionary(nodeInformationMap):
    dictionary= set([])
    for key in nodeInformationMap:
        terms =  nodeInformationMap[key][-1].split(" ")
        twoGrams = []
        for i in range(len(terms)-1):
            twoGrams.append(terms[i]+" "+terms[i+1])
        dictionary = dictionary.union(set(twoGrams))
    print(dictionary)
    handler = open("2-grams","w")
    for term in dictionary:
        handler.write(term+"\n")
    handler.close()


import math

def computeIDF(nodeInformationMap,dictionary):
    counts = {}
    for key in nodeInformationMap:
        terms = set( nodeInformationMap[key][-1].split(" "))
        for term in terms:
            if term in counts:
                counts[term] +=1
            else:
                counts[term] = 1
    handler = open("IDF","w")
    N = len(nodeInformationMap)
    for term in dictionary:
        nT = counts[term]
        handler.write(term+" "+str(math.log(1+N/nT))+"\n")
    handler.close()

def loadDictionary(filename):
    dictionary = open(filename).read().split("\n")
    return dictionary


nodeInformationMap = prepareInformationMap("node_information.csv")
buildDictionary(nodeInformationMap)
oneGrams = loadDictionary("dictionary")
computeIDF(nodeInformationMap,oneGrams)


'''
def extractEdgeInformation(n1,n2):

makeGML("GMLFILE",graph.getDict())

test = open("testing_set.txt","r").read().split("\n")
answer = open("answer001.txt","w")
answer.write("id,category\n")
xAxis =[]
nOverlaps = []
i=0
for example in test:
    xAxis.append(i)
    n1,n2 = example.split(" ")
    nOverlaps.append( graph.neighboorhoodOverlap(n1,n2))
    if graph.neighboorhoodOverlap(n1,n2)>0.01:
        strline = str(i)+",1\n"
        answer.write(strline)
    else:
        strline = str(i) + ",0\n"
        answer.write(strline)


    i+=1
answer.close()
from matplotlib import pyplot as plt
plt.hist(not_connected,bins=100)
plt.show()

plt.scatter(list(range(len(connected))),connected,color="red")
plt.scatter(list(range(len(not_connected))),not_connected,color="blue")
plt.show()
'''