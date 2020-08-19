lista=[]
cont=0
while True:
    N=int(input('Digite um valor: '))
    lista.append(N)
    cont=cont+1
    R=str(input('Deseja continuar? [S/N] ')).strip().upper()
    if R in 'Nn':
        break
lista.sort()
print(lista)
print(f'Foram digitados {cont} valores')
if 5 in lista:
    print('O valor 5 foi está em lista.')
else:
    print('O valor 5 não está na lista.')