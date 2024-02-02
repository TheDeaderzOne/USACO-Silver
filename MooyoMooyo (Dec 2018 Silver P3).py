input = open("mooyomooyo.in","r")
output = open("mooyomooyo.out","w")
GridParam, Connection = [int(x) for x in input.readline().replace("\n","").split()]
PlayerScreen = []; VisitList = []; Que = []; trackers = 0

for x in range(10):
    PlayerScreen.append([])

for _ in range(GridParam):
    arricle = [int(x) for x in list(input.readline().replace("\n",""))]
    for bz in range(10):
        PlayerScreen[bz].append(arricle[bz])

def PuyoPuyoFill(queue,startnodex,startnodey,visitlist,playerscreen,threshold):
    if visitlist[startnodex][startnodey]==1 or playerscreen[startnodex][startnodey]==0:
        return 0
    queue.append([startnodex,startnodey])
    lengthy = 0
    startingnum = playerscreen[startnodex][startnodey]
    visitlist[startnodex][startnodey]=1
    recorder = []
    recorder.append([startnodex,startnodey])
    while len(queue)>0:
        dx = queue[0][0]
        dy = queue[0][1]
        newlist = [[dx+1,dy],[dx-1,dy],[dx,dy+1],[dx,dy-1]]
        for n in newlist:
            if n[0]<10 and n[1]<len(playerscreen[0]):
                if n[0]>-1 and n[1]>-1:
                    if visitlist[n[0]][n[1]]==0:
                        if playerscreen[n[0]][n[1]]==startingnum:
                            recorder.append(n)
                            queue.append(n)
                            visitlist[n[0]][n[1]]=1
        lengthy+=1
        queue.pop(0)
    if lengthy>=threshold:
        global trackers
        trackers+=1
        for h in recorder:
            playerscreen[h[0]][h[1]]=-1
    return playerscreen

x=1

while x>0:
    trackers = 0
    VisitList=[]
    for _ in range(10):
        VisitList.append([0]*GridParam)
    for x1 in range(10):
        for y1 in range(GridParam):
            PuyoPuyoFill(Que,x1,y1,VisitList,PlayerScreen,Connection)
    for x1 in range(10):
        for y1 in range(GridParam):
            if PlayerScreen[x1][y1]==-1:
                PlayerScreen[x1].pop(y1)
                PlayerScreen[x1].insert(0,0)
    if trackers == 0:
        x=0

for ui in range(GridParam):
    for uj in range(10):
        output.writelines(str(PlayerScreen[uj][ui]))
    output.writelines("\n")