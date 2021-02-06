n=list(input('introduceti nr:'))
nrm=0
for i in range(len(n)):
    a=0
    b=0
    c=0
    a=n[i]//100+(n[i]//10)%10
    b=n[i]%10+(n[i]//10)%10
    c=n[i]%10+(n[i]//100)
    if(a==(n[i]%10)) or (b==(n[i]//100)) or c==((n[i]//10)%10):
        nrm+=1
print('nr norocoase sunt', nrm)