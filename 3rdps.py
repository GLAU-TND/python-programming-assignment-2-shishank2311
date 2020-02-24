a=int(input())
l=list()
while(a):
    l.append(a%2)
    a=a//2
k=[l[i] for i in range(len(l)-1,-1,-1)]
l=[]
c=0
for i in k:
    if i==1:
        c+=1
    else:
        l.append(c)
        c = 0
else:
    l.append(c)
max=l[0]
for i in l:
    if max<i:
        max=i
print(max)
