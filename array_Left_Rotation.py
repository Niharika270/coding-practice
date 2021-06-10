n,d=map(int,input().split())
a=list(map(int,input().split()))
print(*a[d:], end=' ')
print(*a[0:d])
