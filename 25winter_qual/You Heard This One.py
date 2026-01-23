import sys
import math
input=sys.stdin.readline

a,b=map(int,input().split())
c=b-a
if c<=0:
    c=1
if  b-a==1:
    print(int(math.log(c,2))+2)
else:
    print(int(math.log(c,2))+1)


