lista=[]

while True:
    P=''
    N=int(input('Digite um valor: '))
    if N in lista:
        print('Valore já existente, não pode ser computador')
    else:
        lista.append(N)
    while P!='S' and P!='N':
        P=str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
    if P=='N':
        break
lista.sort()
print(lista)