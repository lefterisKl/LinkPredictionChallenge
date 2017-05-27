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



def prepareInformationMap(filename):
   information open(filename,"r")


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
