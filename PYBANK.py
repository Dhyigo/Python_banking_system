from sistema import inicio
from interface import menu, gabarito, txtcor


inicio()

catalogo = ['Abrir conta.', 'Entrar.', 'sair.']
login = {}
saldo = 0

try:

    while True:
        opc = menu(lista=catalogo, msg='VENHA PARA O PYBANK!', msgcor=34, corlin=33)

        # abrir conta
        if opc == 1:
            from sistema import abrirConta

            gabarito(txtcor('VOCÊ ESTÁ PERTO DE SE TORNA UM PYCLIENTE!', 34), corlin=33)
            login = abrirConta()
            del abrirConta
            break

        # entrar na conta
        elif opc == 2:

            from sistema import entrar

            gabarito(txtcor('FAÇA LOGIN E APROVEITE TUDO QUE A DE BOM NO PYBANK', 34), corlin=33)
            login = entrar()

            del entrar
            break

        # sair do programa
        elif opc == 3:
            from interface import saindo

            saindo()
            exit()

        else:
            from sistema import aguarde

            print('\033[31mOPÇÃO INVÁLIDA!\nTente uma das opções abaixo.\033[m')
            aguarde(0.4, False)
            del aguarde

except KeyboardInterrupt:
    from interface import saindo
    saindo()


# dentro da conta
catalogo = ['Sacar.', 'Depositar.', 'Ver Movimentações.', 'sair']

try:

    while True:
        from sistema import receberSaldo

        saldo = receberSaldo(login['conta'])

        opc = menu(conta=login['conta'],
                   nome=login['nome'],
                   valor=saldo,
                   lista=catalogo,
                   infor=True, msgcor=34, corlin=33)

        # sacar dinheiro
        if opc == 1:
            from sistema import sacardinheiro, lerdinheiro

            sacar = lerdinheiro('Valor que deseja sacar: R$')
            sacardinheiro(sacar=sacar, conta=login['conta'])
            del sacardinheiro

        # deposistar dinheiro
        elif opc == 2:
            from sistema import depositar, lerdinheiro

            valor = lerdinheiro('Quantos deseja depósitar? R$')
            depositar(valor)

        # extrato bancário
        elif opc == 3:
            from sistema import extratos
            extratos(login['conta'])

        # sair do programa
        elif opc == 4:
            from interface import saindo

            saindo()
            break

        else:
            from sistema import aguarde

            print('\033[31mOPÇÃO INVÁLIDA!\nTente uma das opções abaixo.\033[m')
            aguarde(0.4, False)
            del aguarde
except KeyboardInterrupt:
    from interface import saindo

    saindo()

except KeyError:
    pass
