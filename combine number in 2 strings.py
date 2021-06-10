a=input()
b=input()
x=[]
y=[]
for i in a:
    if i.isdigit():
        x.append(i)
for i in b:
    if i.isdigit():
        y.append(i)
for i in range(min(len(x),len(y))):
    print(int(x[i]),end='')
    print(int(y[i]),end='')
if len(x)>len(y):
    print(''.join(x[i:]))
else:
    print(''.join(y[i:]))


'''
a=input()
b=input()
x=[]
y=[]
for i in a:
    if i.isdigit():
        x.append(i)
for i in b:
    if i.isdigit():
        y.append(i)
if len(x)>len(y):
    for i in range(len(x)):
        print(x[i],end='')
        if i<len(y):
            print(y[i],end='')
elif(len(x)==len(y)):
    for i in range(len(x)):
        print(x[i],end='')
        if i<len(y):
            print(y[i],end='')
else:
    for i in range(len(y)):
        if i<len(x):
            print(x[i],end='')
        print(y[i],end='')
'''
