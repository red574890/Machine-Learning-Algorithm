
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load and process the data
dataset=pd.read_csv(r'/Users/hsuyunhuung/Documents/機器學習/hw1_15_train.dat.txt',sep=" ",header=None)
dataset[3],dataset[4]=dataset[3].str.split("\t",1).str

dataset.insert(0,"constant",1) # add constant value (X0)



wt=(0,0,0,0,0)
wt=np.array(wt)
wpocket=(0,0,0,0,0)
wpocket=np.array(wpocket) #initialize the pocket
times=0
least_error=0
rate=0
exp=0
ar=0

dataset = dataset.sample(frac=1).reset_index(drop=True) #shuffle the dataset
while(times<=100):   # we will run the iteration 100 times.
    error=0
    for i in range(0,len(dataset)):
        x=[float(dataset["constant"][i]),float(dataset[0][i]),float(dataset[1][i]),float(dataset[2][i]),float(dataset[3][i])]
        x=np.array(x)
        y=float(dataset[4][i])
        if(np.sign(np.dot(wt.T, x))!=y): #check how much error does current w has
            error+=1
            w=y*np.array(x)            #wt=w+yx
        if(times==0):
            least_error=error
            wt=w+wt
        if(error>0):
            wt=w+wt
        if(least_error>error):
            print(error)
            
            wpocket=w+wt            # put the w with least error into pocket
            print(wpocket)
            least_error=error
    times+=1


# load the test data to check the correct rate


testdata=pd.read_csv(r'/Users/hsuyunhuung/Documents/機器學習/hw1_18_test.dat.txt',sep=" ",header=None)
testdata[3],testdata[4]=testdata[3].str.split("\t",1).str
testdata.insert(0,"constant",1) # add constant value (X0)

terror=0
for i in range(0,len(testdata)):
    x=[float(testdata["constant"][i]),float(testdata[0][i]),float(testdata[1][i]),float(testdata[2][i]),float(testdata[3][i])]
    x=np.array(x)
    y=float(testdata[4][i])
    if(np.sign(np.dot(wt.T, x))!=y):
        terror+=1

print("The accuracy is "+str((len(testdata)-terror)/len(testdata)*100)+"%")
