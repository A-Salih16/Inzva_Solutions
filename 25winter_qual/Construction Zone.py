import sys
input=sys.stdin.readline

N,K=map(int,input().split())
if N<4 and N!=1:
    print("NO")

elif N==4:
    if K==1 or  K==4:
        print("NO")
    else:
        print("YES")


else:
    print("YES")