input = open("moocast.in","r")
output = open("moocast.out","w")
CowNum = int(input.readline().replace("\n",""))
CowCoordList=[]; PowerList = []; AdjList = []

for _ in range(CowNum):
    x1,y1,power = [int(x)for x in input.readline().replace("\n","").split()]
    CowCoordList.append([x1,y1])
    PowerList.append(power)
    AdjList.append([])

for ind in range(CowNum):
    for h in range(CowNum):
        if h == ind:
            pass
        else: 
            difference = (CowCoordList[h][0]-CowCoordList[ind][0])**2 + (CowCoordList[h][1]-CowCoordList[ind][1])**2
            if difference <= (PowerList[ind])**2:
                AdjList[ind].append(h)
                
Visited = [0]*CowNum
Queue = []

def BFS(adjlist,startnode,queue,visitlist):
    length=0
    queue.append(startnode)
    visitlist[startnode]=1
    while len(queue)>0:
        for x in adjlist[queue[0]]:
            if visitlist[x]==0:
                queue.append(x)
                visitlist[x]=1
        length+=1
        queue.pop(0)
    return length

maxk = 0
for xj in range(CowNum):
    Visited = [0]*CowNum
    maxk = max(maxk, BFS(AdjList,xj,Queue,Visited))

output.writelines(str(maxk))