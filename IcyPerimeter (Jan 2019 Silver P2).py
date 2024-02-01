input = open("perimeter.in","r")
output = open("perimeter.out","w")
NumRowsColumns = int(input.readline().replace("\n",""))
FloodFill = []; Visits = []; Queue = []; maxis = [0,0]

for x in range(NumRowsColumns):
    arry = list(input.readline().replace("\n",""))
    FloodFill.append(arry)
    Visits.append([0]*NumRowsColumns)

def FloodFillsy (queue,visitlist,startx,starty,floodfill):
    if floodfill[startx][starty]=="." or visitlist[startx][starty]==1:
        return [0,0]
    queue.append([startx,starty])
    visitlist[startx][starty]=1
    area = 0
    perimeter = 0
    while len(queue)>0:
        tempx=queue[0][0]
        tempy=queue[0][1]
        tempadjlist = [[tempx-1,tempy],[tempx+1,tempy],[tempx,tempy-1], [tempx,tempy+1]]
        for u in tempadjlist:
            if u[0] > -1 and u[1] > -1:
                if u[0] < len(floodfill) and u[1] < len(floodfill):
                    if visitlist[u[0]][u[1]]==0:
                        if floodfill[u[0]][u[1]]=="#":
                            queue.append(u)
                            visitlist[u[0]][u[1]]=1
                        else:
                            perimeter+=1
                else:
                    perimeter+=1
            else:
                perimeter+=1
        area+=1
        queue.pop(0)
    return [area,perimeter]

for x in range(NumRowsColumns):
    for y in range(NumRowsColumns):
        exe = FloodFillsy(Queue,Visits,x,y,FloodFill)
        if exe[0]>maxis[0]:
            maxis = exe
        elif exe[0]==maxis[0]:
            if exe[1]<maxis[1]:
                maxis=exe

output.writelines(str(maxis[0])+ " "+str(maxis[1]))