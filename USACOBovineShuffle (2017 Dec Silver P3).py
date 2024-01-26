input = open("shuffle.in","r")
output = open("shuffle.out","w")

Num = int(input.readline().replace("\n",""))

BovineShuffle = [int(d)-1 for d in input.readline().replace("\n","").split()]

FunctionalGraph = []

for y in range(len(BovineShuffle)):
    FunctionalGraph.append(BovineShuffle[y])

FinalSet = set()

def TurtleandHare(graph,startnode):
    global FinalSet
    z=0
    turtle = graph[graph[startnode]]
    hare = graph[graph[graph[startnode]]]
    countset = set()
    if turtle==hare:
        countset.add(turtle)
    while turtle != hare:
        turtle = graph[turtle]
        hare = graph[graph[hare]]
        if turtle in FinalSet:
            z=1
            break
    if z==0:
        hare=graph[hare]
        countset.add(hare)
        while turtle!=hare:
            hare=graph[hare]
            countset.add(hare)
    return countset
for l in range(Num):
    if l in FinalSet:
        pass
    else:
        FinalSet.update(TurtleandHare(FunctionalGraph,l))

output.writelines(str(len(FinalSet)))