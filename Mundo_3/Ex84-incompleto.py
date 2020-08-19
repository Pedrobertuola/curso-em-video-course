lista=[]
temp=[]
peso=[]
cont=0
while True:
    temp.append(str(input('Nome: ')))
    N=(int(input('Peso: ')))
    temp.append(N)
    peso.append(N)
    lista.append(temp[:])
    temp.clear()
    cont=cont+1
    R=str(input('Deseja continuar?[S/N]'))
    if R in 'Nn':
        break

print(lista)
print(f'Quantidade de pessoas cadastradas: {cont} ')
print(f'O maior peso foi de:{max(peso)}')

print(f'O menor peso foi de : {min(peso)}')