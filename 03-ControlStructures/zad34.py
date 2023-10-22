pln=int(input('Enter amount in pln: '))
piec=0
dwa=0
jeden=0
while pln>0:
    if pln/5:
        piec=piec+1
       # pln=pln//5
    if pln/2:
        dwa=dwa+1
        #pln=pln//2
    if pln/1:
        jeden=jeden+1
       # pln=pln//1

print(piec, dwa, jeden)

