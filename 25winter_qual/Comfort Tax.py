import sys
input=sys.stdin.readline
N=int(input())
liste=list(map(int,input().split()))
prefix=[]
a=sum(liste[:3])
prefix.append(a)

for i in range(3,N):
    a=a-liste[i-3]+liste[i]
    prefix.append(a)
lol=len(prefix)
cnt=0
for i in range(lol):
    if prefix[i]<0:
        cnt+=abs(prefix[i])
        if i+1<lol:
            prefix[i+1]+=abs(prefix[i]) 
        if i+2<lol:
            prefix[i+2]+=abs(prefix[i])
        prefix[i]=0
print(cnt) 