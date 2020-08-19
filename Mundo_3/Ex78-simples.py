valores=[]
for cont in range(0,5):
    valores.append(int(input(f'Para a posição {cont} digite um valor: ')))
print(valores)
print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')