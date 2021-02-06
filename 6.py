l=[]
l.extend(input())
l=[int(i) for i in l]
n=0
for i in range(len(l)):
    n= n*10 + l[i]
print(n)