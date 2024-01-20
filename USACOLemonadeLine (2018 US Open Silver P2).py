input = open("lemonade.in","r"); output = open("lemonade.out","w")
input.readline()
lemonadeline = sorted([int(x) for x in input.readline().replace("\n","").split()])
counter = 0
while lemonadeline[-1]>=counter:
    counter+=1
    lemonadeline.pop(-1)
output.writelines(str(counter))