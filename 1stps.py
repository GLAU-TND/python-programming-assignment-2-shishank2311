l=eval(input())
count=0
k=[i[0] for i in l]
m=[i[-1] for i in l]
for i in k:
    if i not in m:
         count=1
         print("cannot be circled")
         break
else:
    print("can be circled")
if count!=1:
    n=list()
    n.append(l[0])
    for i in n:
        for j in range(1,len(l)):
            if i[-1]==l[j][0]:
                n.append(l[j])
                del l[j]
                break
    print(n)
