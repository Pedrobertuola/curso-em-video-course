T=('zero','Um','Dois','Três','Quatro','Cindo','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze',
   'Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    N=int(input('Digite um número de 0 a 20: '))
    if 0<=N<=20:
        break
    else:
        print('Erro!Digite um valor entre 0 e 20')
print(f'você digitou o número {T[N]}')