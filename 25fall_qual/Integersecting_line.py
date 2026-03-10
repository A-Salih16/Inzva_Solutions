r,c=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
gr=[]
xmax=max(x1,x2)
xmin=min(x1,x2)
ymax=max(y1,y2)
ymin=min(y1,y2)
for  _ in range(r):
    gr.append(["."]*c)
    
    
if x1==x2:
    for j in range(ymin, ymax+1):
        gr[j][x1]="#"
else:
    a=(y1-y2)/(x1-x2)
    b=y1-a*x1
    for i in range(xmin, xmax+1):
        y_val=a*i+b
        if abs(y_val-round(y_val))<1e-9:
            j=int(round(y_val))
            if ymin<=j<=ymax:
                gr[j][i]="#"
    
              
for y in range(r-1,-1,-1):
    print("".join(gr[y]))
