a=int(input())
liste=list(map(int,input().split()))
INF= float('inf')
summax=float('inf')
cc=sum(liste)
for i in range(len(liste)):
    if abs(cc-liste[i])<summax:
        summax=abs(cc-liste[i])
        
print(summax)
    
    




