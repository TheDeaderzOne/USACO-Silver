input = open("cowdance.in","r")
output = open("cowdance.out","w")
import math

Num, TMax = [int(x) for x in input.readline().replace("\n","").split()]

CowTimes=[]

for x in range(Num):
    CowTimes.append(int(input.readline().replace("\n","")))

def checkerfuncsy(length,CowTime):
    TehList = list(CowTime[:length])
    ChallengerList = list(CowTime[length:len(CowTime)])
    TehList.sort()
    TehList = [TMax-j for j in TehList]
    while len(ChallengerList)>0:
        yut = ChallengerList.pop(0)
        if yut in TehList:
            TehList.remove(yut)
        elif yut<TehList[0]:
            TehList[0]-=yut
            TehList.sort(reverse=True)
        else:
            return False
    return True

def bihsearch(arr):
    leftpointer = 0
    rightpointer = len(arr)-1

    while leftpointer != rightpointer:
        mid = math.ceil((leftpointer+rightpointer)/2)
        if checkerfuncsy(mid,CowTimes):
            rightpointer = mid-1
        else:
            leftpointer = mid
    
    return leftpointer+1

output.writelines(str(bihsearch(CowTimes)))
