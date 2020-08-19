from time import sleep


def ajuda(com):
    """
    -> Exibe a ajuda interativa de um "comando" do Python.
    :param func: (Obrigatório) Função que será exibida a ajuda interativa do Python.
    :return: Sem retorno.
    """

    título(f'Acessando o manual do comando \'{com}\'', cor='azul')
    print(cores['branco'])
    help(com)
    print(end=cores['sem'])
    sleep(2)


def título(msg, cor='sem'):
    """
    -> Escreve um título com a cor desejada na tela.
    :param msg: (obrigatório) A mensagem que será exibida na tela.
    :param cor: (opcional) A cor em que o texto será exibido.
    :return: Sem retorno.
    """
    tam = len(msg) + 6
    print(end=cores[cor])
    print('~' * tam)
    print(f'|  {msg}  |')
    print('~' * tam)
    print(end=cores['sem'])
    sleep(1)


# Programa Principal
cores = {'sem': '\033[m',  # Limpa cor
         'vermelho': '\033[1;41m',
         'verde': '\033[1;42m',
         'azul': '\033[1;44m',
         'branco': '\033[7m'
         }

while True:
    título('SISTEMA DE AJUDA PyHELP', cor='verde')
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    ajuda(comando)

título('ATÉ LOGO!', cor='vermelho')