try:
    n=int(input())
    for __ in range(n):
        D,d,P,Q=map(int,input().split())
        z=(D%d)
        x=(D//d)
        y=x-1
        if D%d==0:
            t=(P*x*d)+((y*x*Q*d)/2)
        else:
            t=(P*x*d)+((y*x*Q*d)/2)+(P+Q*x)*z
        print(int(t))
except EOFError as e:
    print(end='')
