aprov={}
partidas=[]
aprov['nome']=str(input('Nome do jogador: '))
tot=int(input('Digite a quantidade de partidas: '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c}: ')))
aprov['gols']=partidas[:]
aprov['total']=sum(partidas)
print(aprov)
print('-=-'*30)
for k,v in aprov.items():
    print(f'O campo {k} tem valor {v}.')
print('-=-'*30)
print(f'O jogador {aprov["nome"]} jogou {tot} partidas.')
for i,v in enumerate(aprov['gols']):
    print(f'=> Na partida {i} , fez {v} gols')