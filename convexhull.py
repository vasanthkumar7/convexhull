import pandas as pd

import numpy as np
import math
from matplotlib import pyplot as plt
x=[1,3,1,7,9,5,3,2,7,5,4,4,5]
y=[2,4,3,8,3,6,8,6,3,8,5,4,5]

xx=[]
yy=[]
for i in range(len(x)):
    if(x[i]!=y[i]):
        xx.append(x[i])
        yy.append(y[i])
tempx=x
tempy=y
x=xx
y=yy

p=min(y)
pp=y.index(p)

q=x[pp]
x.remove(q)
y.remove(p)
x.insert(0,q)
y.insert(0,p)
e=0
distances=[]
for i in range(1,len(x)):
    d=math.sqrt((x[0]-x[i])**2+(y[0]-y[i])**2)
    db=math.sqrt((x[0]-x[i])**2)
    a=np.degrees(np.arccos(db/d))
    distances.append(int(a))
print(distances)

for i in range(len(distances)):
    mi=i
    for j in range(i+1,len(x)-1):
        if(distances[mi]>distances[j]):
            mi=j
    if(mi!=i):
        temp=x[mi+1]
        x[mi+1]=x[i+1]
        x[i+1]=temp
        temp=y[mi+1]
        y[mi+1]=y[i+1]
        y[i+1]=temp
        temp=distances[mi]
        distances[mi]=distances[i]
        distances[i]=temp
    
stackx=[]
stacky=[]
stackx.append(x[e])
stacky.append(y[e])
stackx.append(x[e+1])
stacky.append(y[e+1])
stackx.append(x[e+2])
stacky.append(y[e+2])
try:
    anglep=((stacky[e+1]-stacky[e])*(stackx[e+2]-stackx[e+1]))-((stacky[e+2]-stacky[e+1])*(stackx[e+1]-stackx[e]))
except ZeroDivisionError:
    anglep=0

if(anglep>=0):
    del stackx[e+1]
    del stacky[e+1]
if(anglep<0):
    e=e+1
print("e=",e)
print("angle= ",anglep)
print(" ")
for i in range(len(stackx),len(x)):
        stackx.append(x[i])
        stacky.append(y[i])
       
        w=0
        wq=0
        print(stackx,stacky,sep=' ')
       
        try:
            angle=((stacky[e+1]-stacky[e])*(stackx[e+2]-stackx[e+1]))-((stacky[e+2]-stacky[e+1])*(stackx[e+1]-stackx[e]))
        except ZeroDivisionError:
            angle=0
        
        print(stackx[e+1])
        print(stacky[e+1])
        if(angle>=0):
            del stackx[e+1]
            del stacky[e+1]
        if(angle<0):
            e=e+1
        print("angle=",angle)
        print(stackx,stacky,sep=' ')
        
        print("e=",e)
        print(" ")
       

stackx.append(stackx[0])
stacky.append(stacky[0])
kpk=len(stackx)
stax=[]
stay=[]

        
        
print(stackx,stacky,sep=' ')

plt.title("convex hull") 
plt.plot(stackx,stacky)
plt.plot(tempx,tempy,'o')
plt.show()
    
print(stackx,stacky,sep=' ')
