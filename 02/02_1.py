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


print(f'read {len(reports)} reports')
safeReports = 0
for report in reports:
    level=(report[1] - report[0]) > 0
    isSafe = True
    for i in range(0,len(report)-1):
        if ((report[i+1] - report[i]) > 0) != level:
            print("level not OK. unsafe.")
            isSafe = False  
        diff = abs(report[i+1]-report[i])
        if (diff < 1 or diff > 3):
            print(f"diff to high! {report[i+1]} - {report[i]} = {diff}")
            isSafe = False
    if isSafe:
        safeReports = safeReports + 1

print(f'{safeReports} safe reports.')