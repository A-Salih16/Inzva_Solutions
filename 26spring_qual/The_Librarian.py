n=int(input())
liste=list(map(int,input().split()))
for i in range(1,n):
    liste[i]=liste[i]+liste[i-1]

q=int(input())
ql=[]
for _ in range(q):
    a=int(input())
    ql.append(a)
k=0
for i in ql:
    if i<=liste[0]:
        print(1,i)
    else:
        l=0
        r=n-1
        
        while r>l:
            mid=(l+r)//2
            if liste[mid]>=i:
                r=mid
            else:
                l=mid+1
            k=l
        print(k+1,i-liste[k-1])
    
        
    
            