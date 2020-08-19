lista=[]
listap=[]
listai=[]
while True:
    N=int(input('Digite um valor: '))
    lista.append(N)
    if N%2==0:
        listap.append(N)
    else:
        listai.append(N)

    R=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if R=='N':
        break

print(f'Lista total : {lista}')
print(f'Lista de valores pares: {listap}')
print(f'Lista de valores impares: {listai}')