temp=[]
lista=[]
mai=men=0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso: ')))
    if len(lista)==0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<men:
            men=temp[1]
    lista.append(temp[:])
    temp.clear()

    R=str(input('Deseja continuar?[S/N] '))
    if R in 'Nn':
        break
print(f'Ao todo você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi {mai}Kg',end=' ')
for p in lista:
    if p[1]==mai:
        print(f'[{p[0]}]')
print(f'O menor peso foi {men}kg',end=' ')
for p in lista:
    if p[1]==men:
        print(f'[{p[0]}]')