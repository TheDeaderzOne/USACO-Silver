import math
input = open("angry.in","r")
output = open("angry.out","w")
HayBales, CowNumber = [int(x) for x in input.readline().replace("\n","").split()]
haybalepos = []

for reads in input.readlines():
    numb = int(reads.replace("\n","").split()[0])
    haybalepos.append(numb)

haybalepos.sort()
optimizerange = math.ceil((haybalepos[-1]-haybalepos[0])/(2*CowNumber))

def checkerfuncbinary(array,cownum,inputnumber):
    tracker = array[0]
    for _ in range(cownum):
        firstpattern = int(tracker+(2*inputnumber))
        for bruh in range(len(haybalepos)):
            if haybalepos[bruh]>firstpattern:
                tracker = array[bruh]
                break
            if bruh == len(haybalepos)-1:
                return True
    return False

def binaryfalsetotrue(num):
    leftpointer = 0
    rightpointer = num
    while leftpointer!=rightpointer:
        midpoint = math.ceil((leftpointer+rightpointer)/2)
        if checkerfuncbinary(haybalepos,CowNumber,midpoint):
            rightpointer = midpoint-1
        else:
            leftpointer=midpoint
    return leftpointer+1

output.writelines(str(binaryfalsetotrue(optimizerange)))