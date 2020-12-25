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
        X.append([1,x1,x2,x1*x2,x1*x1,x2*x2])
        Y.append([y])
    return np.mat(X),np.array(Y)


    
def error(func,x,y):
    y1=func(x)
    errorNum=len(y[y1!=y])
    return errorNum/len(y)

def A(X):
    Y=[]
    for i in range(len(X)):
        temp=np.array(X[i])
        Y.append([sign(-1-1.5*temp[0,1]+0.08*temp[0,2]+0.13*temp[0,3]+0.05*temp[0,4]+1.5*temp[0,5])])
    return np.array(Y)

def B(X):
    Y=[]
    for i in range(len(X)):
        temp=np.array(X[i])
        Y.append([sign(-1-1.5*temp[0,1]+0.08*temp[0,2]+0.13*temp[0,3]+0.05*temp[0,4]+0.05*temp[0,5])])
    return np.array(Y)

def C(X):
    Y=[]
    for i in range(len(X)):
        temp=np.array(X[i])
        Y.append([sign(-1-0.05*temp[0,1]+0.08*temp[0,2]+0.13*temp[0,3]+1.5*temp[0,4]+1.5*temp[0,5])])
    return np.array(Y)

def D(X):
    Y=[]
    for i in range(len(X)):
        temp=np.array(X[i])
        Y.append([sign(-1-0.05*temp[0,1]+0.08*temp[0,2]+0.13*temp[0,3]+15*temp[0,4]+1.5*temp[0,5])])
    return np.array(Y)

def E(X):
    Y=[]
    for i in range(len(X)):
        temp=np.array(X[i])
        Y.append([sign(-1-0.05*temp[0,1]+0.08*temp[0,2]+0.13*temp[0,3]+1.5*temp[0,4]+15*temp[0,5])])
    return np.array(Y)


if __name__=='__main__':
    x,y=generateX(1000)
    print("Prop 14")
    print("A is "+str(error(A,x,y)))
    print("B is "+str(error(B,x,y)))
    print("C is "+str(error(C,x,y)))
    print("D is "+str(error(D,x,y)))
    print("E is "+str(error(E,x,y)))
    print("Prop 15")
    errorSum=0
    for i in range(1000):
        x,y=generateX(1000)
        errorSum+=error(C,x,y)

    print("Average error is "+str(errorSum/1000))
    
    
    

        
