import sys
input=sys.stdin.readline

N,K=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

a=A[0]
b=B[0]



for i in range(1, N):
    new_a=min(a+A[i],b+A[i]+K)
    new_b=min(b+B[i],a+B[i]+K)
    a,b=new_a,new_b

print(min(a, b))
