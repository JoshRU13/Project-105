import math
import csv
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    data1=list(reader)
data=data1[0]
def mean(data):
    m=len(data)
    total=0
    for x in data:
        total=total+int(x)
    mean=total/m
    return mean
square=[]
for i in data:
    a = int(i)-mean(data)
    a= a **2
    square.append(a)
some=0
for i in square:
    some=some+i
result = some/(len(data)-1)
final=math.sqrt(result)
print(final)
