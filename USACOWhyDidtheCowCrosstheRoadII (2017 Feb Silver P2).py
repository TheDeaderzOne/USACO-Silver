input = open("maxcross.in","r")
output = open("maxcross.out","w")

Ne,Ke,Be=[int(x)for x in input.readline().replace("\n","").split()]

RoadCross=([int(1) for _ in range(Ne)])

for _ in range(Be):
    RoadCross[int(input.readline().replace("\n",""))-1]=0

minsignallist = []

minsignallist.append(RoadCross[:Ke].count(0))
for r in range(int(Ne-Ke)):
    if RoadCross[r]==0 and RoadCross[int(r+Ke)]==1:
        minsignallist.append(int(minsignallist[r])-1)
    elif RoadCross[r]==1 and RoadCross[int(r+Ke)]==0:
        minsignallist.append(int(minsignallist[r])+1)
    else:
        minsignallist.append(int(minsignallist[r]))

output.writelines(str(min(minsignallist)))