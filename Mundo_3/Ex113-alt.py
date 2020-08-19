def leiaint(msg):
    while True:
        try:
            n=int(input(msg))

        except:
            print('Por favor, digite um valor válido')
        else:
            print(f'Valor {n} computado com sucesso')
            break

def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print('\033[31mPor favor, digite um valor válido\033[m')
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            break
        else:
            print(f'Valor {n} computado com sucesso')
            break

#num=leiaint('Digite um valor:')

leiafloat('Digite um valor: ')
