
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as rd




def sign(x):
    if(x>0):
        return 1
    elif(x<0):
        return -1

def decision_stump(data,d):
    minerror=100
    verse=False
    global Finalv
    global delta
    Finalv=False
    #enumerating all the possible combination
    for i in range(0,len(data)):
        error=0
        serror=0
        for j in range(0,len(data)):
            if(data[d][j]<data[d][i]):
                y1=-1
            else:
                y1=1

            if(data[10][j]!=y1):
                error+=1
        for j in range(0,len(data)):
            if(data[d][j]<data[d][i]):
                y1=1
            else:
                y1=-1

            if(data[10][j]!=y1):
                serror+=1
        if(serror<error):
            error=serror
            verse=True
        if(error<minerror):
            minerror=error
            Finalv=verse
            delta=data[d][i]
            
    return minerror

def decision_stump2(data,d,delta,verse):
    error=0
    if(verse==True):
        for i in range(0,len(data)):
            if(data[d][i]<delta):
                y1=1
            else:
                y1=-1

            if(data[10][i]!=y1):
                error+=1
    else:
        for i in range(0,len(data)):
            if(data[d][i]<delta):
                y1=-1
            else:
                y1=1

            if(data[10][i]!=y1):
                error+=1
 
            
    return error

                
        
d=1
minerror=100

dataset1 = pd.read_csv('/Users/hsuyunhuung/Documents/機器學習/hw2/hw2_train.dat.txt',sep=' ',header=None)

#for each dimension 
#i~d find the best decision stump 
#using the one-dimensional decision stump algorithm that you have just implemented.



while(d<10):
    error=decision_stump(dataset1,d)
    if(error<minerror):
        minerror=error
        dim=d
    d+=1

print("Best error rate "+str(minerror/len(dataset1)*100)+"%")
print("dimension "+str(dim-1))
print("Delta is "+str(delta))


    


# validate test data


testdata = pd.read_csv('/Users/hsuyunhuung/Documents/機器學習/hw2/hw2_test.dat.txt',sep=' ',header=None)


print("test data error rate: "+str(decision_stump2(testdata,dim,delta,Finalv)/len(testdata)*100)+"%")



