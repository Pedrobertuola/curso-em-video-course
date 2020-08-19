def ficha():
    j = str(input('Nome do jogador: '))
    g = str(input('Gols marcados: '))
    if len(j) == 0:
        j = '<Desconhecido>'
    if g.strip() == '':
        g = 0
    print(f'O jogador {j} marcou {g} gol(s) no campeonato.')

ficha()