def inicio():
    from arquivo import (criarpasta,
                         criarArquivo,
                         attArquivo
                         )
    try:
        criarpasta('dados')
        criarpasta('user')
        criarArquivo('user', 'user')
        criarArquivo(newarq='id', pasta='user')
        attArquivo(1000)
    except FileExistsError:
        pass


def entrar():
    tentativa = 1
    tempo = 30

    while True:

        from arquivo import lerlinha

        login = {'nome': validaentrada('NOME: '), 'doc': validaentrada('DOCUMENTO: '),
                 'conta': int(validaentrada('CONTA: ', sonum=True, aviso='Digite apenas números'))}
        try:

            dados = lerlinha('user', 'user', pos=(login['conta'] - 1000))
            dados = dados.split(';')

        except IndexError:
            if tentativa == 3:
                aguarde(tempo)
                tempo *= 3
                tentativa = 0

        except Exception as erro:
            print(f'\033[31mERRO{erro}\n\033[32mTente novamente\033[m')

        else:
            if dados[0] == login['nome'] and dados[1] == login['doc']:
                return login

        tentativa += 1
        print(f'\033[31mCONTA INVÁLIDA!\033[m')


def aguarde(tempo, msg=True):
    from time import sleep
    if msg:
        print(f'\033[31mAguarde {tempo} segundos...\033[m')
    sleep(tempo)


def abrirConta():
    from arquivo import lerlinha
    from interface import txtcor

    conta = int(lerlinha('id'))

    novo_nome = validaentrada('NOME: ', aviso='Digite seu nome corretamente')
    novo_documento = validaentrada('NÚMEROS DO DOCUMENTO: ', sonum=True,
                                   aviso='Digite 4 números ao todo!', maximo=4, minimo=4)
    from interface import carregando
    from arquivo import verificar

    if not verificar(arquivo='user', pasta='user', documento=novo_documento):
        from arquivo import escrever, attArquivo, criarArquivo
        data = pegardata()

        novo_usuario = {'nome': novo_nome, 'doc': novo_documento, 'conta': conta}
        escrever('user', 'user', f'{novo_nome};{novo_documento};{conta};{data}')

        criarArquivo(newarq=conta)
        criarArquivo(newarq=f'd{conta}')
        escrever('dados', f'd{conta}', 0)

        carregando('CRIANDO CONTA')

        attArquivo(conta + 1)
        return novo_usuario

    else:
        print(txtcor('CONTA JÁ EXISTE!'))


def validaentrada(msg, maximo=40, minimo=1, sonum=False, aviso='valor errado'):
    try:
        while True:
            entrada = ''

            if sonum:
                from interface import leianum
                entrada = str(leianum(f'{msg}'))

            else:
                entrada = str(input(f'{msg}')).strip().capitalize()

            if minimo <= len(entrada) <= maximo:
                return entrada
            else:
                from interface import txtcor
                print(txtcor(f'{aviso}'))

    except KeyboardInterrupt:
        from interface import saindo, txtcor
        print(txtcor('Usuário descidiu cancelar :('))
        saindo()
        exit()


def receberSaldo(conta):
    from arquivo import lerlinha

    saldo = lerlinha(arquivo=f'd{conta}',
                     pasta='dados')
    return float(saldo)


def pegardata():
    from datetime import date
    data = date.today()
    data = str(data.strftime('%d/%m/%Y'))
    return data


def sacardinheiro(sacar, conta):
    from interface import linha
    linha(cor=33)
    valor = sacar
    saldo = int(receberSaldo(conta))

    if saldo >= sacar:
        from interface import dinheiro
        from arquivo import escrever

        data = pegardata()
        valores = (100, 50, 20, 10, 5, 2, 1)
        cont = pos = 0
        cedula = valores[pos]

        escrever(pasta='dados', arquivo=conta,
                 texto=f'saque de;\033[31m-{dinheiro(sacar)}\033[m;Data: {data}')
        while True:
            try:
                if sacar >= cedula:
                    sacar -= cedula
                    cont += 1

                else:
                    if cont > 0:
                        from interface import dinheiro
                        nome = 'cédula' if cedula > 1 else 'moeda'
                        nome += 's' if cont > 1 else ''
                        print(f'{cont} {nome} de {dinheiro(cedula)}')
                        aguarde(2, False)
                    pos += 1
                    cont = 0
                    cedula = valores[pos]

                    if sacar == 0:
                        saldo -= valor
                        from arquivo import attArquivo
                        attArquivo(dados=saldo,
                                   arquivo=f'd{conta}',
                                   pasta='dados')
                        return saldo
            except (KeyboardInterrupt, IndexError):
                pass

    else:
        from interface import txtcor
        print(txtcor('SALDO INSUFICIENTE'))
        aguarde(3, msg=False)


def depositar(deposito):
    from arquivo import attArquivo, escrever, arquivoExiste
    from interface import dinheiro, txtcor, linha

    data = pegardata()
    conta = validaentrada('CONTA: ', sonum=True,
                          aviso='Conta inválida!', maximo=4, minimo=4)
    if arquivoExiste(arq=conta):
        saldo = receberSaldo(int(conta))
        saldo += deposito

        attArquivo(dados=saldo,
                   arquivo=f'd{conta}',
                   pasta='dados')
        escrever(pasta='dados', arquivo=conta,
                 texto=f'Depósito de; \033[32m{dinheiro(deposito)}\033[m;Data: {data}')

        linha(cor=33)
        print(txtcor(f'Depósito feito com sucesso para a conta {conta}.', cor=32))
        aguarde(2, msg=False)

    else:
        print(txtcor('Conta inválida!'))
        aguarde(3, msg=False)


# att
def transferir():
    pass


def extratos(conta):
    from arquivo import lerlinhas
    from interface import txtcor

    extrato = lerlinhas(pasta='dados', arquivo=conta)

    if len(extrato) > 0:
        from interface import linha

        linha(cor=33)
        for v in extrato:
            v = v.replace('\n', '')
            v = v.split(';')  # dividir em: 1° ind. frase, 2° valor R$, 3° data.
            print(f'{v[0]:11} {v[1]:33} {v[2]}')
            aguarde(0.5, False)

    else:
        print(txtcor('Vazio.'))
    aguarde(1, False)


def lerdinheiro(msg='Digite um valor: R$', aviso='Valor inválido!'):
    while True:
        valor = input(f'{msg}').strip()
        valor = f'{valor}'.replace(',', '_').replace('.', '').replace('_', '.')
        try:
            valor = float(valor)
        except ValueError:
            from interface import txtcor
            print(txtcor(f'{aviso}'))

        else:
            if valor <= 10000:
                return valor
            else:
                from interface import txtcor
                print(txtcor(f'Valor máximo permitido é R$ 10.000,00.', cor=33))


if __name__ == '__main__':
    sacardinheiro(436, 1000)
