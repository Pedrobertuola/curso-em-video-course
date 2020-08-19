valores=[]

maior=0
menor=0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))
    if c==0:
        maior=menor=valores[c]
    else:
        if valores[c]>maior:
            maior=valores[c]
        if valores[c]<menor:
            menor=valores[c]
print(valores)
print(f'O maior valor foi {maior} na posição{valores.index(max(valores))}')
print(f'O menor valor foi {menor} na posição {valores.index(min(valores))}')
