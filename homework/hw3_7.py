import math

def E(u,v):
    res=math.exp(u)+math.exp(2*v)+math.exp(u*v)+u*u-2*u*v-3*u-2*v
    return res


def gu(u,v):
    return math.exp(u)+math.exp(u*v)*v+2*u-2*v-3

def gv(u,v):
    return 2*math.exp(2*v)+math.exp(u*v)*u-2*u+4*v-2

def main():
    n=0
    a=0.01
    u=0
    v=0
    while(n<5):
        tempu=u-a*gu(u,v)
        tempv=v-a*gv(u,v)
        u=tempu
        v=tempv
        n+=1

    print(E(u,v))

if __name__ == '__main__':
    main()
