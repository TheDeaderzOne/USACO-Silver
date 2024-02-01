input = open("rental.in","r")
output = open("rental.out","w")
CowInt,Milkings,Sales = [int(x) for x in input.readline().replace("\n","").split()]
Cows = []
MilkingList=[]
SaleList = []
for x in range(CowInt):
    Cows.append(int(input.readline().replace("\n","")))

for i in range(Milkings):
    MilkingList.append([int(x) for x in input.readline().replace("\n","").split()])

for j in range(Sales):
    SaleList.append(int(input.readline().replace("\n","")))

Cows.sort()
MilkingList.sort(key=lambda x: x[1])
SaleList.sort()

Cows.reverse()
pointermilk = len(MilkingList)-1
pointersale = 0
total = 0

for obj in range(CowInt):
    milkprice = 0
    SpecificCow = Cows[obj]

    if SpecificCow<MilkingList[pointermilk][0]:
        MilkingList[pointermilk][0]-=SpecificCow
        milkprice += SpecificCow*MilkingList[pointermilk][1]

    elif SpecificCow==MilkingList[pointermilk][0]:
        milkprice += MilkingList[pointermilk][0]*MilkingList[pointermilk][1]
        if pointermilk>0:
            pointermilk-=1

    else:
        while SpecificCow>MilkingList[pointermilk][0]:
            milkprice += MilkingList[pointermilk][0]*MilkingList[pointermilk][1]
            SpecificCow-=MilkingList[pointermilk][0]
            MilkingList[pointermilk][0]=0
            if pointermilk==0:
                break
            else:
                pointermilk-=1

        if SpecificCow<MilkingList[pointermilk][0]:
            MilkingList[pointermilk][0]-=SpecificCow
            milkprice += SpecificCow*MilkingList[pointermilk][1]

        elif SpecificCow==MilkingList[pointermilk][0]:
            milkprice += MilkingList[pointermilk][0]*MilkingList[pointermilk][1]
            if pointermilk>0:
                pointermilk-=1
    
    if Sales<(CowInt-obj):
        total+=milkprice

    else:
        sellprice = SaleList[pointersale]
        maxy = max(sellprice,milkprice)
        total+=maxy
        pointersale+=1

output.writelines(str(total))