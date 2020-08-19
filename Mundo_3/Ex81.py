lista=[]
cont=0
while True:
    R=''
    N=int(input('Digite um valor: '))
    lista.append(N)
    while R!='S' and R!='N':
        R=str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    cont=cont+1
    if R=='N':
        break
lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {cont} valores')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')