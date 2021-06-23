c,n,m=map(int,input().split())
k=list(map(int,input().split()))
u=list(map(int,input().split()))
mc=0
a=[]
for i in range(0,n):
    for j in range(0,m):
        if ((k[i]+u[j])-c)<=0:
            mc=k[i]+u[j]
            a.append(mc)
if len(a)==0:
    print(-1)
else:
    print(max(a))
