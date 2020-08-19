listagem=('Lapis',1.75,
          'Borracha',2,
          'Mochila',20,
          'Transferidor',10,
          'Relogio',100)
print('='*40)
print(f'{"Listagem de preços":^40}')
print('='*40)
for pos in range(0,len(listagem)):
    if pos%2==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)