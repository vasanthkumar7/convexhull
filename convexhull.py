import pandas as pd
from matplotlib import pyplot as plt
x=[1,3,1,7,9,5,5,4,3,2]
y=[2,4,3,8,3,6,5,4,8,6]
p=min(y)
pp=y.index(p)

q=x[pp]
x.remove(q)
y.remove(p)
x.insert(0,q)
y.insert(0,p)
e=0
stackx=[]
stacky=[]
stackx.append(x[e])
stacky.append(y[e])
stackx.append(x[e+1])
stacky.append(y[e+1])
stackx.append(x[e+2])
stacky.append(y[e+2])
try:
    anglep=((stacky[e+1]-stacky[e])/(stackx[e+1]-stackx[e]))-((stacky[e+2]-stacky[e+1])/(stackx[e+2]-stackx[e+1]))
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
            angle=((stacky[e+1]-stacky[e])/(stackx[e+1]-stackx[e]))-((stacky[e+2]-stacky[e+1])/(stackx[e+2]-stackx[e+1]))
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
        

print(stackx,stacky,sep=' ')
plt.title("convex hull") 
plt.plot(stackx,stacky)
plt.plot(x,y,'o')
plt.show()
    
print(stackx,stacky,sep=' ')

