import pandas as pd
from matplotlib import pyplot as plt
x=[1,3,1,9,5,5,4,3,2]
y=[2,4,3,3,6,5,4,8,6]
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
angle=((stackx[e+2]-stackx[e+1])/(stacky[e+2]-stacky[e+1]))-((stackx[e+1]-stackx[e])/(stacky[e+1]-stacky[e]))
if(angle>=0):
    stackx.remove(x[e+1])
    stacky.remove(y[e+1])
if(angle<0):
    e=e+1

    
print(stackx,stacky,sep=' ')

for i in range(len(stackx)+1,len(x)):
        stackx.append(x[i])
        stacky.append(y[i])
        w=0
        wq=0
        
        try:
            angle=((stackx[e+2]-stackx[e+1])/(stacky[e+2]-stacky[e+1]))-((stackx[e+1]-stackx[e])/(stacky[e+1]-stacky[e]))
        except ZeroDivisionError:
            angle=0
        if(angle>=0):
            stackx.remove(stackx[e+1])
            stacky.remove(stacky[e+1])
        if(angle<0):
            e=e+1
       


        
stackx.append(stackx[0])
stacky.append(stacky[0])
plt.title("convex hull") 
plt.plot(stackx,stacky)
plt.plot(x,y,'o')
plt.show()
    
print(stackx,stacky,sep=' ')

