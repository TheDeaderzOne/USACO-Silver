input = open("pairup.in","r")
output = open("pairup.out","w")
manualincrement=0
TimeList = []
for line in input.readlines():
    if manualincrement == 1:
        CowsAndTime = line.replace("\n","").split()
        CowsAndTime = [int(x) for x in CowsAndTime]
        TimeList.append(CowsAndTime)
    else:
        manualincrement=1

TimeList.sort(key=lambda xd:xd[1])

def CowFunc(array):
    firstpointer = 0
    lastpointer = len(array)-1
    maxlen = 0
    while firstpointer <= lastpointer:
        maxlen = max(array[firstpointer][1]+array[lastpointer][1], maxlen)
        if array[firstpointer][0]-array[lastpointer][0]==0:
            firstpointer+=1
            lastpointer-=1
        elif array[firstpointer][0]-array[lastpointer][0]>0:
            array[firstpointer][0]=int(array[firstpointer][0]-array[lastpointer][0])
            lastpointer-=1
        else:
            array[lastpointer][0]=int(array[lastpointer][0]-array[firstpointer][0])
            firstpointer+=1
    return maxlen

output.writelines(str(CowFunc(TimeList)))