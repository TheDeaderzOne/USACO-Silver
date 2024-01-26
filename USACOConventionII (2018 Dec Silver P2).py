input = open("convention2.in","r")
output = open("convention2.out","w")

CowNum=int(input.readline().replace("\n",""))

CowDemands = []
CowTracker = 1
for bheg in input.readlines():
    temper=[int(zed)for zed in bheg.replace("\n","").split()]
    temper.append(CowTracker)
    CowDemands.append(temper)
    CowTracker+=1
    
CowDemands.sort()

waitingtime = []

def EatingOrder(DemandList,TempList):
    firsteaterinfo = DemandList.pop(0)
    Time=(firsteaterinfo[0]+firsteaterinfo[1])
    Waiting = 0

    while len(DemandList)>0 or len(TempList)>0:
        while len(DemandList)>0 and DemandList[0][0]<=Time:
            if DemandList[0] in TempList:
                pass
            else:
                TempList.append(DemandList[0])
                DemandList.pop(0)

        if len(TempList) == 0:
            TempList.append(DemandList[0])
            DemandList.pop(0)

        poppedcow = min(TempList, key=lambda z: z[2])
        TempList.remove(poppedcow)
        Waiting = max(Waiting,Time-poppedcow[0])
        Time = max(Time+poppedcow[1], poppedcow[0]+poppedcow[1])
    return Waiting

output.writelines(str(EatingOrder(CowDemands,waitingtime)))