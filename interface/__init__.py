def gabarito(msg, corlin=32):
    """
    Formata texto.
    :param corlin: cor da linha.
    :param msg: Recebe o texto.
    :return: retorna gabarito para o terminal.
    """
    linha(cor=corlin)
    print(msg.center(60))
    linha(cor=corlin)


def carregando(msg='Carregando', cor=32):
    """
    Efeito de load.
    :param msg: mensagem a ser exibida.
    :param cor: número da cor da mensagem.
    :return: Efeito de load no terminal.
    """
    from time import sleep

    print(f'\033[{cor}m{msg}', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.\033[m')


def saindo():
    """
    Efeito de load com mensagem 'finalizando programa'.
    :return: mensagem 'finalizando programa' na tela.
    """
    carregando(msg='Finalizando programa', cor=31)


def linha(tam=60, cor=32):
    """
    Gerar linha.
    :param cor: Número da cor.
    :param tam: Tamanho da linha.
    :return: Retorna linha para o terminal.
    """
    print(f'\033[{cor}m-\033[m' * tam)


def txtcor(msg, cor=31):
    """
    Deixa a mensagem colorida.
    :param msg: mensagem a ser exibida.
    :param cor: número da cor.
    :return: mensagem com cor.
    """
    return f'\033[{cor}m{msg}\033[m'


def leianum(msg='Digite um número: '):
    """
    ler um número.
    :param msg: Texto que vai sugir no prompt
    :return: Retorna o número
    """

    while True:
        try:
            entrada = int(input(f'{msg}'))
        except ValueError:
            print(txtcor('VALOR INVÁLIDO!'))
        else:
            return entrada


def menu(msg='BEM VINDO(A) AO PYBANK!', conta='', nome='', valor='', lista='', infor=False, corlin=32, msgcor=33):
    """
    Mostra o menu de opções.
    :return: Renorna o valor da opção.
    """
    print('\033[33m', end='')
    gabarito(txtcor(msg, msgcor), corlin=corlin)
    if infor:
        print(f'\033[mCONTA: \t{conta}')
        print(f'NOME: \t{nome:<30}SALDO: \033[32m{dinheiro(valor)}\033[m\n')
    for cont, opcao in enumerate(lista):
        print(f'\033[33m{cont + 1}- \033[34m{opcao.upper()}\033[m')
    linha(cor=corlin)
    opc = leianum('Escolha uma das opções: ')
    return opc


def dinheiro(valor, moeda='R$'):
    """
    Formata os valores em modelos de dinheiro.
    :param valor: Valor a ser formatado.
    :param moeda: (opcional) símbolo da moeda.
    :return: Retorna o valor formatado.
    """
    valor = f'{moeda}{valor:,.2f}'.replace(',', '_') \
        .replace('.', ',').replace('_', '.')
    return valor


# testes
if __name__ == '__main__':
    menu()
    carregando()
    gabarito('BEM VINDO AO PYBANK')
    leianum()
