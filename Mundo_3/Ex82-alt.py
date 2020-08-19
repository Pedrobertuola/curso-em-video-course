lista=[]
par=[]
impar=[]
while True:
    N=int(input('Digite um valor: '))
    lista.append(N)

    R=str(input('Quer continuar?[S/N] '))
    if R in 'Nn':
        break
for i,v in enumerate(lista):
    if v%2==0:
        par.append(v)
    elif v%2==1:
        impar.append(v)
print(lista)
print(f'lista par: {par}')
print(f'lista impar: {impar}')