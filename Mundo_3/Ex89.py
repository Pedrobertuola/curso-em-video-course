temp=[]
total=[]
cont=0
while True:
    nome=str(input('Nome: '))
    temp.append(nome)
    n1=float(input('Primeira nota: '))
    temp.append(n1)
    n2=float(input('Segunda nota: '))
    temp.append(n2)
    M=(n1+n2)/2
    temp.append(M)
    total.append(temp[:])
    temp.clear()
    cont=cont+1
    R=str(input('Quer continuar? [S/N]'))
    if R in 'Nn':
        break
print(total)
print('-=-'*30)
print('Boletim')
print('-=-'*30)
for d in range(0,cont):
    print(f'{d+1}o aluno   Nome:{total[d][0]:15}   Media:{total[d][3]:4}')
A=0
while True:
    A=int(input('Digite o numero do aluno que deseja consultar: '))
    if A==999:break
    print(f'Aluno:{total[A-1][0]}...... Primeira nota: {total[A-1][1]} .... Segunda nota :{total[A-1][2]}')


