import re
import numpy as np

with open("1.txt", encoding='gb18030', errors='ignore') as f:
    data = f.read()
i=0
a = {}
b = {}
c = {}
while data != '':
    a[i]=data[data.find("["):data.find("]")+1]
    i=i+1
    data=data[data.find("]")+1:]
l=len(a)
for i in range(0,l):
    b[i]=a[i].find("\"评论数\": ")
    b[i]=a[i][b[i]+10:b[i]+15]
    b[i]=re.findall(r'\d+',b[i])
avg=sum(b)/l
for i in range(0,l):
    c[i]=np.var(b[i][0])
d=sum(c)/l
for i in range(0,l):
    b[i]=(b[i]-avg)/(d**0.5)
    if b[i]>1:
        with open("1.txt","a") as f:
            f.write(a[i])