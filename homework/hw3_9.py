import math
import numpy as np

def E(u,v):
    res=math.exp(u)+math.exp(2*v)+math.exp(u*v)+u*u-2*u*v-3*u-2*v
    return res

def gu(u,v):
    return math.exp(u)+math.exp(u*v)*v+2*u-2*v-3

def gv(u,v):
    return 2*math.exp(2*v)+math.exp(u*v)*u-2*u+4*v-2

def duu(u,v):
    return math.exp(u)+math.exp(u*v)*(v*v)+2

def dvv(u,v):
    return 4*math.exp(2*v)+math.exp(u*v)*(u*u)+4

def duv(u,v):
    return math.exp(u*v)+math.exp(u*v)*(u*v)-2

def Hessian(u,v):
    hession=np.mat([[duu(u,v),duv(u,v)],[duv(u,v),dvv(u,v)]])
    return hession

def main():
    n=0
    u=0
    v=0
    while(n<5):
        H=Hessian(u,v)
        grad=np.array([[gu(u,v)],[gv(u,v)]])
        delta=H.I*grad
        u-=float(delta[0])
        v-=float(delta[1])
        n+=1

    print(E(u,v))

if __name__ == '__main__':
    main()
