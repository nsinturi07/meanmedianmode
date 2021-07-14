import csv
with open("height-weight.txt",newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    n=filedata[i][1]
    newdata.append(float(n))
l=len(newdata)
total=0
for x in newdata:
    total=total+x
    mean=total/l
print("mean"+str(mean))
