n=int(input('introduceti nr :'))
nrm=0
nr=[]
i=2
while i<n:
    a=n
    b=i
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    if b==1:
        nrm +=1
        nr.append(i)
    i +=1
print(f'cantitatea de nr prime:',nrm, 'nr gasite:', nr)
