l=list(eval(input('introduceti nr:')))
n=0
for i in range(len(l)):
    a=0
    b=0
    a=l[i]//1000+(l[i]//100)%10
    b=(l[i]//10)%10+l[i]%10
    if(a==b):
        n+=1
print('nr norocoase:', n)

