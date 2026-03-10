a=list(map(str,input().split()))
T1=[int (a[0][0]),int(a[0][1]),int(a[0][3]),int(a[0][4]),int(a[0][6]),int(a[0][7])]
T2=[int (a[1][0]),int(a[1][1]),int(a[1][3]),int(a[1][4]),int(a[1][6]),int(a[1][7])]
cnt=0


while(T1[0]!=T2[0] or T1[1]!=T2[1] or T1[2]!=T2[2] or T1[3]!=T2[3] or T1[4]!=T2[4] or T1[5]!=T2[5]):
    if (T1[0]==T1[5] and T1[1]==T1[4] and T1[2]==T1[3]):
        cnt+=1
    T1[5]+=1
    
    if(T1[5]==10):
        T1[5]=0
        T1[4]+=1
        if(T1[4]==6):
            T1[4]=0
            T1[3]+=1
            if(T1[3]==10):
                T1[3]=0
                T1[2]+=1
                if(T1[2]==6):
                    T1[2]=0
                    T1[1]+=1
                    if(T1[1]==10):
                        T1[1]=0
                        T1[0]+=1


                        
if (T1[0]==T1[5] and T1[1]==T1[4] and T1[2]==T1[3]):
        cnt+=1


print(cnt)