lista=[]
while True:
    N=int(input('Digite um valor: '))
    lista.append(N)
    R=str(input('Quer continuar? [S/N]'))[0]
    if R in 'Nn':
        break
        print('Saindo')
lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {len(lista)} valores')
if 5 in lista:
    print(f'O valor 5 está na posição {lista.index(5)+1}')
else:
    print('O valore 5 não foi digitado')
