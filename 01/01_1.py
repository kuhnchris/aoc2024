import os

readAll=[]
with open("01.txt","r") as f:
    readAll=f.readlines()


listLeft = []
listRight= []
for rIn in readAll:
    r=rIn.strip()
    rr=r.split(" ")
    listLeft.append(rr[0])
    listRight.append(rr[3])

def findDistIter1():
    lMin = min(listLeft)
    rMin = min(listRight)
    dist = abs(int(lMin)-int(rMin))
    print(f'minLeft: {lMin} minRight: {rMin} dist: {dist} ')
    listLeft.remove(lMin)
    listRight.remove(rMin)
    return dist

finalDist = 0
while len(listLeft) != 0:
    finalDist = finalDist + findDistIter1()
    
print(f"final distance: {finalDist}")