l=eval(input())
n=list()
for i in range(len(l)):
    l[i]=str(l[i])
b=[i for i in l]
n=['0' for i in l]
n[0]='0'
k=0
for i in range(len(n)):
    for j in b:
        if int(j+n[i])>int(n[i]+j):
            n[i]=j
            k=j
    if k==0:
        k=n[i]
    l=[s for s in b]
    b=[]
    flag=0
    for p in l:
        if flag==0:
            if p!=k:
                b.append(p)
            else:
                flag+=1
        else:
            b.append(p)
    print(b)
for i in n:
    print(i,end="")
