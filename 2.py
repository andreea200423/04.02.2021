N=[]
N.extend(input())
N=[int(i) for i in N]
if N==sorted(N):
    print('cifre nr formeaza o consecutivtate strict crescatoare')
else:
    print('cifre nr nu formeaza o consecutivtate strict crescatoare')