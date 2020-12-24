import numpy as np
import random

def func(x1,x2):
    if((x1*x1+x2*x2-0.6)>=0):
        return 1
    elif((x1*x1+x2*x2-0.6)<0):
        return -1

def sign(x):
    if(x>=0):
        return 1
    else:
        return -1

def generateX(N):
    X=[]
    Y=[]
    for i in range(0,N):
        x1=random.uniform(-1,1)
        x2=random.uniform(-1,1)
        y=func(x1,x2)
        noise=random.random()
        if(noise<=0.1):
            y=-y
        X.append([1,x1,x2])
        Y.append([y])
    return np.mat(X),np.array(Y)

def findw(X,Y):
    pseudo_inverse=np.linalg.pinv(X)
    w=pseudo_inverse*Y
    return w


    
def error(w,x,y):
    y1=x*w
    y1[y1>=0]=1
    y1[y1<0]=-1
    errorNum=len(y[y1!=y])
    return errorNum/len(y)

if __name__=='__main__':
    errorSum=0
    for i in range(1000):
        x,y=generateX(1000)
        w=findw(x,y)
        errorSum+=error(w,x,y)
    print(errorSum/1000)
    
    

        
