import numpy as np
import pandas as pd


def sita(s):
    return 1/(1+np.exp(-s))


def d_Ein(w,train):
    n=len(train)
    total=0
    
    for i in range(0,n):
        y=int(train.iloc[i,20:21])
        xn=np.array(train.iloc[i,:20])
        s=-1*y*np.dot(w.T,xn)
        total+=sita(s)*-y*xn
    res=total/n
    return res

def sign(x):
    if(x>0):
        return +1
    else:
        return -1

def evulate(w,test):
    n=len(test)
    error=0
    for i in range(0,n):
        y=int(test.iloc[i,20:21])
        xn=np.array(test.iloc[i,:20])
        s=np.dot(w.T,xn)
        if(sign(sita(s))!=y):
            error+=1
    return error/n
    



if __name__ == '__main__':
    train=pd.read_csv("/Users/hsuyunhuung/Documents/機器學習/hw3_18-20/hw3_train.dat.txt",sep=" ",header=None)
    test=pd.read_csv("/Users/hsuyunhuung/Documents/機器學習/hw3_18-20/hw3_test.dat.txt",sep=" ",header=None)
    train=train.drop(columns=[0])
    test=test.drop(columns=[0])
    T=0
    error=0
    while(T<101):
        n=0
        wt=np.zeros(20)
        while(n<200):
            wt=wt-0.001*d_Ein(wt,train)
            if(sum(wt)<=0.001):
                break
        error+=evulate(wt,test)
        T+=1
    
    print(error/101)

