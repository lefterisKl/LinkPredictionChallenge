lines = open("IDF","r").split("\n")
idfs=[]
for line in lines:
    term,score = line.split(" ")
    idfs.append((term,score))

sortedIdfs = sorted(idfs, key=lambda x: x[1])

fil
