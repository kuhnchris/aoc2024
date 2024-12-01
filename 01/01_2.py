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

def findLeftInRight():
    findElem = listLeft.pop(0)
    cnt = 0
    for e in listRight:
        if findElem == e:
            cnt = cnt + 1
    retval = int(findElem) * cnt
    print(f'findElement: {findElem} - count: {cnt} - returns: {retval}')
    return retval

finalDist = 0
while len(listLeft) != 0:
    finalDist = finalDist + findLeftInRight()
    
print(f"final value: {finalDist}")