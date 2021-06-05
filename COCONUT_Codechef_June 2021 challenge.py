try:
    n=int(input())
    for __ in range(n):
        x1,y1,x2,y2=map(int,input().split())
        a=b=0
        if x2%x1 !=0:
            a=a+(x2//x1)+1
        else:
            a=a+(x2//x1)

        if y2%y1 !=0:
            b=b+(y2//y1)+1
        else:
            b=b+(y2//y1)

        print(a+b)
except EOFError as e:
    print(end='')
