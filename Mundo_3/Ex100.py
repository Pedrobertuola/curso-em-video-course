from random import randint

def sorteando(lista):
    print('Sorteando 5 valores da lista')
    for c in range(1,6):

        lista.append(randint(1,10))
def somapar(n):
    soma=0
    for cont in n:
        if cont%2==0:
            soma=soma+cont

    print(f'A soma dos números pares é {soma}')


lista=[]
sorteando(lista)
somapar(lista)
print(lista)

