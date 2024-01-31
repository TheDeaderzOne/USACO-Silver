input = open("fenceplan.in","r")
output = open("fenceplan.out","w")
import math

NCows, MPairs = [int(x) for x in input.readline().replace("\n","").split()]

CowCoordinates = []; MooNetworks = []
for _ in range(NCows):
    be = [int(x) for x in input.readline().replace("\n","").split()]
    CowCoordinates.append(be)
    MooNetworks.append([])

for _ in range(MPairs):
    Cow1,Cow2 = [int(x)-1 for x in input.readline().replace("\n","").split()]
    MooNetworks[Cow1].append(Cow2)
    MooNetworks[Cow2].append(Cow1)

minperimeter = math.inf

EsQueue = []
VisitedArr = [0]*NCows

def MooBFS (queue,startnode,visitlist, asjlist, cordlist):
    if visitlist[startnode]==1:
        return math.inf
    else:
        queue.append(startnode)
        visitlist[startnode]=1
        tempminx = math.inf; tempminy = math.inf; tempmaxy = 0; tempmaxx = 0
        while len(queue)>0:
            for x in asjlist[queue[0]]:
                if visitlist[x]==0:
                    queue.append(x)
                    visitlist[x]=1
            x1,y1 = cordlist[queue[0]]
            if x1<tempminx:
                tempminx = x1
            if x1>tempmaxx:
                tempmaxx=x1
            if y1<tempminy:
                tempminy = y1
            if y1>tempmaxy:
                tempmaxy=y1
            queue.pop(0)
        return int(2*(tempmaxx-tempminx))+(2*(tempmaxy-tempminy))

for x in range(NCows):
    minperimeter = min(minperimeter,MooBFS(EsQueue,x,VisitedArr,MooNetworks,CowCoordinates))

output.writelines(str(minperimeter))