def fatorial(N,show=False):
    """"
    Calcula o fatorial de um número
    :param N:O número a ser calculado.
    :param show:(opcional) mostrar ou não a conta.
    :return:O valor do fatorial de um número N.

    """
    fat=1
    for c in range(N,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print(' x ',end='')
            else:
                print(' = ',end='')

        fat=fat*c

    return fat

print(fatorial(4, show=True))
help(fatorial)