time=[]
jogador={}
partidas=[]
while True:
    jogador.clear
    jogador['nome']=str(input('Nome do jogador: '))
    tot=int(input('Digite a quantidade de partidas: '))
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp=str(input('Quer continuar?[S/N]')).upper()[0]
        if resp in 'SN':
            break
    print('Erro! responda apenas S ou N')
    if resp=='N':
        break
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
        print()
print('-'*40)

