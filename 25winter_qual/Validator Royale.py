import sys
input=sys.stdin.readline
n=int(input())
a=[]
for _ in range(n):
    b=input().rstrip()
    
    a.append(b)

def mirr(list1):
    dup=list1[0]
    cnt=1
    for i  in range(1,len(list1)):
        if dup==list1[i]:
            cnt+=1
        else:
            dup=list1[i]
            cnt=1
        if cnt==2:
            return 1
    return 0

def dup3(list1):
    dup=list1[0]
    cnt=1
    for i  in range(1,len(list1)):
        if dup==list1[i]:
            cnt+=1
        else:
            dup=list1[i]
            cnt=1
        if cnt>=3:
            return 1
    return 0

def clash(liste):
    c=set(liste)
    
    if len(c)>8:
        return 0
    if dup3(liste):
        return 0
    ismir=mirr(liste)
    if ismir and len(c)==8:
        return 0
    if ismir:
        c.add("mirror")
    dict={}
    for i in c:
        dict[i]=1
    liste2=liste.copy()
    for i in range(1,len(liste)):
        if liste[i]==liste[i-1]:
            liste2[i]="mirror"
    liste=liste2.copy()
    for i in range(len(liste)):
        if i>=5:
            dict[liste[i-5]]=1
        
        dict[liste[i]]-=1
        if dict[liste[i]]<0:
            return 0
    return 1

if clash(a):
    print("VALID")
else:
    print("INVALID")