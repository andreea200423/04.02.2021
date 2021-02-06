N=int(input('numarul: '))
pare=0
impare=0
while N != 0:
    if(N % 10) % 2 == 0:
        pare+=1
    else:
        impare+=1
    N //=10
print(f'nr de cifre impare e {impare}, iar nr de cifre pare e {pare}')