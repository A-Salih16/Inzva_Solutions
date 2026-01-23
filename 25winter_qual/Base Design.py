import sys
input=sys.stdin.readline
t=int(input())

def maxi(log):
    liste=[]
    a,b=log[0],log[1]
    x,y=log[2],log[3]

    for i in range(4):    
        if i==0:
            if y-1>=0:
                liste.append(a*(y))
            else:
                liste.append(0)
        if i==1:
            
            if x-1>=0:
                liste.append(b*x)
            else:

                liste.append(0)
                
        if i==2:
            if y+1<b:
                liste.append((b-y-1)*a)
            else:
                liste.append(0)
            
            
        if i==3:
            if x+1<a:
                liste.append((a-x-1)*b)
            else:
                liste.append(0)
    return liste


for _ in range(t):
    l=list(map(int,input().split()))
    print(max(maxi(l)))




