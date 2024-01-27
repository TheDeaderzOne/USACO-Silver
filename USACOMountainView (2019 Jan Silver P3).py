input = open("mountains.in","r")
output = open("mountains.out","w")
input.readline()

MountainCords = []

CoveredCords=[]

for uo in input.readlines():
    ji = [int(o)for o in uo.replace("\n","").split()]
    MountainCords.append(ji)

MountainCords.sort()

for x in MountainCords:
    x.append("P")
    CoveredCords.append(x)

for i in range(len(MountainCords)): 
    tracker = 1
    if len(CoveredCords[i])>2:
        while i-tracker>-1 and MountainCords[i][1]-(MountainCords[i][0]-MountainCords[i-tracker][0])>-1:
            if MountainCords[i][1]-(MountainCords[i][0]-MountainCords[i-tracker][0]) >= CoveredCords[i-tracker][1]:
                CoveredCords[i-tracker]=[MountainCords[i-tracker][0], MountainCords[i][1]-(MountainCords[i][0]-MountainCords[i-tracker][0])]
            else:
                break
            tracker +=1
        tracker =  1
        while tracker+i<len(MountainCords) and MountainCords[i][1]-(MountainCords[tracker+i][0]-MountainCords[i][0])>-1:
            if MountainCords[i][1]-(MountainCords[tracker+i][0]-MountainCords[i][0]) >= CoveredCords[i+tracker][1]:
                CoveredCords[i+tracker]=[MountainCords[i+tracker][0], MountainCords[i][1]-(MountainCords[tracker+i][0]-MountainCords[i][0])]
            else:
                break
            tracker +=1

y=0
for x in CoveredCords:
    if len(x)==3:
        y+=1

output.writelines(str(y))