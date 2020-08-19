def ficha(jog='<Desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


N=str(input('Nome do jogador:'))
G=str(input('Número de gols: '))
if G.isnumeric():
    G=int(G)
else:
    G=0
if N.strip()=='':
    ficha(gol=G)
else:
    ficha(N,G)
