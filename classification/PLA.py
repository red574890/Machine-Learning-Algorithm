import matplotlib.pyplot as plt
import numpy as np


dataset = np.array([
((1, -0.4, 0.3), -1),
((1, -0.3, -0.1), -1),
((1, -0.2, 0.4), -1),
((1, -0.1, 0.1), -1),
((1, 0.9, -0.5), 1),
((1, 0.7, -0.9), 1),
((1, 0.8, 0.2), 1),
((1, 0.4, -0.6), 1),
((1, 0.8, -0.8), 1)])


wt=(0,0,0)
wt=np.array(wt)
stop=False
while(stop==False):
    error=0
    for x, s in dataset:
        if(np.sign(np.dot(wt.T, x))!=s):
            error+=1
            w=s*np.array(x)
    if(error>0):
        wt=w+wt
    elif(error==0):
        print(wt)
        stop==True
        break

x_positive=dataset[dataset[:,1]==1]
x_negative=dataset[dataset[:,1]==-1]
x_positive=x_positive[:,0]
x_negative=x_negative[:,0]
a=[]
b=[]
for i in x_positive:
	a.append(i[1])
	b.append(i[2])

c=[]
d=[]

for i in x_negative:
	c.append(i[1])
	d.append(i[2])
plt.scatter(a,b,c='b', marker="o")
plt.scatter(c,d,c='r', marker="x")

x_values=[0,wt[1]]
y_values=[0,wt[2]]

plt.plot(x_values, y_values)
l = np.linspace(-2,2)
a,b = -wt[2]/wt[1], -wt[0]/wt[2]
plt.plot(l, a*l + b, 'b-')
plt.show()
    


        
    
