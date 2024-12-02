import os

readAll=[]
with open("02.txt","r") as f:
    readAll=f.readlines()

reports=[]
for rIn in readAll:
    r = rIn.strip()
    rS = r.split(" ")
    reportLine = []
    for rV in rS:  
        reportLine.append(int(rV))
    reports.append(reportLine)

def testLevel(currentReport):
    level=(currentReport[1] - currentReport[0]) > 0
    isSafe = True
    for i in range(0,len(currentReport)-1):
        if ((currentReport[i+1] - currentReport[i]) > 0) != level:
            #print("level not OK. unsafe.")
            isSafe = False  
        diff = abs(currentReport[i+1]-currentReport[i])
        if (diff < 1 or diff > 3):
            #print(f"diff to high! {currentReport[i+1]} - {currentReport[i]} = {diff}")
            isSafe = False
    return isSafe    

print(f'read {len(reports)} reports')
safeReports = 0
for report in reports:
    isSafe = testLevel(report)
    if isSafe:
        safeReports = safeReports + 1
    else:
        for i in range(0,len(report)):
            stripReport = report.copy()
            del stripReport[i]
            #print(stripReport)
            isSafe = testLevel(stripReport)
            if isSafe:
                print("Fault-solver fixed report.")
                safeReports = safeReports + 1
                break
            

print(f'{safeReports} safe reports.')