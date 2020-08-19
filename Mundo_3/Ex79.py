lista=[]
while True:
    n=int(input('Digite um valor:'))
    if n not in lista:
        lista.append(n)

    R=str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if R in'Nn':
        break
lista.sort()
print(lista)
