n=int(input())
p=int(input())
if p==1:
    print(0)
else:
    if n%2==0:
        a=p//2
        b=(n-p)//2
        if (n-p)==1:
            b=1
        print(min(a,b))
    else:
        a=p//2
        b=(n-p)//2
        print(min(a,b))
        
        
