

import numpy as np
import pandas as pd
import random as rd




def sign(x):
    if(x>0):
        return 1
    elif(x<0):
        return -1

def decision_stump(data):
    all_error=[]
    minerror=20
    #enumerating all the possible combination
    for i in range(0,len(data)):
        error=0
        for j in range(0,len(data)):
            if(data['x'][j]<=data['x'][i]):
                y1=-1
            else:
                y1=1

            if(data['y'][j]!=y1):
                error+=1
        if(error<minerror):
            minerror=error
    return minerror

def generate():
    x = []
    y = []

    for i in range(0,20): #Generate X
        x.append(rd.random()*2-1)
    x=sorted(x)
    noise=0
    for i in range(0,20): #Generate y with 20% noise
        ran = rd.random()
        if(ran<0.2):
            y.append(-1*sign(x[i]))
            noise+=1
        else:
            y.append(sign(x[i]))

    dataset=pd.DataFrame({'x':x,'y':y},columns=["x","y"])
    return dataset
                
        
times=0
allerror=0    

while(times<100):
    dataset=generate()
    error=decision_stump(dataset)
    allerror+=error
    times+=1

print(allerror/(20*100))
    
