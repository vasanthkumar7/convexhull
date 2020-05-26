import pandas as pd

import numpy as np
import math
from matplotlib import pyplot as plt
#this will work for  distict points
x=[5,6,7,3,2,1,7,9,2,6]
y=[4,5,3,2,5,7,3,5,1,2]
for i in range(len(x)-1):
    mi=i
    for j in range(i+1,len(x)):
        if(x[mi]>x[j] and y[mi]>y[j]):
            mi=j
    if mi!=i:
        temp=x[i]
        x[i]=x[mi]
        x[mi]=temp
        temp=y[i]
        y[i]=y[mi]
        y[mi]=temp
        
print(min(x))
xx=[]
yy=[]
for i in range(len(x)):
    if x[i]!=y[i] or y[i]==min(y[i]):
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
print(distances)
print(x,y,sep=' ')
    
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

for i in range(len(stackx),len(x)):
        stackx.append(x[i])
        stacky.append(y[i])
       
        w=0
        wq=0
       
       
        try:
            angle=((stacky[e+1]-stacky[e])*(stackx[e+2]-stackx[e+1]))-((stacky[e+2]-stacky[e+1])*(stackx[e+1]-stackx[e]))
        except ZeroDivisionError:
            angle=0
        
        
        if(angle>=0):
            del stackx[e+1]
            del stacky[e+1]
            if(len(stackx)>=2):
                try:
                    anglep=((stacky[e]-stacky[e-1])*(stackx[e+1]-stackx[e]))-((stacky[e+1]-stacky[e])*(stackx[e]-stackx[e-1]))
                except ZeroDivisionError:
                    anglep=0
                if(anglep>=0):
                    del stackx[e]
                    del stacky[e]
                    e=e-1
                
           

           

            
            
        if(angle<0):
            e=e+1
        print(stackx,stacky,sep=' ')
        
       

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
