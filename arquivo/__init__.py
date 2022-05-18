def arquivoExiste(arq, pasta='dados'):
    """
    Verifica se o arquivo ja existe.
    :param arq: nome do arquivo.
    :param pasta: pasta onde o arquivo pode estar.
    :return: True(arquivo existe), False(arquivo não existe)
    """
    try:
        arquivo = open(f'{pasta}//{arq}.txt', 'r')

    except FileNotFoundError:
        return False

    else:
        arquivo.close()
        return True


def criarpasta(pasta):
    """
    gerador de pasta
    :param pasta: nome da pasta
    :return: None
    """
    from os import makedirs
    makedirs(pasta)


def criarArquivo(newarq, pasta='dados'):
    """
    Criar arquivos.
    :param newarq: Nome do novo arquivo txt
    :param pasta: pasta onde deve ser criado
    :return: True
    """
    if not arquivoExiste(newarq, pasta):
        try:
            arquivo = open(f'{pasta}//{newarq}.txt', 'w+', encoding="utf-8")

        except FileNotFoundError:
            criarpasta(pasta)
            criarArquivo(newarq, pasta)

        else:
            arquivo.close()

    return True


def escrever(pasta, arquivo, texto):
    """
    escrve em um arquivo txt.
    :param pasta: Nome da pasta
    :param arquivo: Nome do arquivo
    :param texto: texto que deseja escrever
    :return: None
    """
    try:
        with open(f'{pasta}//{arquivo}.txt', 'a+', encoding='UTF-8') as arq:
            arq.writelines(f'{texto}\n')

    except FileNotFoundError:
        criarpasta(pasta)
        escrever(pasta, arquivo, texto)


def lerlinha(arquivo='id', pasta='user', pos=0):
    """
    ler linha de um arquivo txt.
    :param pos: linha onde deseja ler(OBS: 0 é a primeira linha).
    :param arquivo: nome do arquivo.
    :param pasta: nome da pasta onde o arquivo esta.
    :return: retorna a linha em formato string.
    """

    txt = ''

    with open(f'{pasta}//{arquivo}.txt', 'r', encoding="utf-8") as linha:
        txt = linha.readlines()
        txt = txt[pos].replace('\n', '')

    return txt


def lerlinhas(arquivo, pasta='dados'):
    """
    Ler um arquivo txt e retorna uma lista de dicionaior com nome, documento e conta.
    :param arquivo: Nome do arquivo txt.
    :param pasta: Nome da pasta.
    :return: uma lista com dados.
    """

    with open(f'{pasta}//{arquivo}.txt', 'r', encoding="utf-8") as linhas:
        lista = linhas.readlines()
    return lista


def verificar(documento, arquivo='user', pasta='user'):
    """
    Verifica se a pessoa existe nos registros.
    :param arquivo: nome do arquivo(por padrão é user)
    :param pasta: nome da pasta(por padrão é user)
    :param documento: documento da pessoa questão.
    :return: True se foi encontradoe False se não encontrado.
    """
    lista = lerlinhas(arquivo, pasta)
    encontrou = cont = 0

    while len(lista) > cont:
        v = lista[cont].split(';')

        if documento == v[1]:
            encontrou += 1
            break

        cont += 1

    if encontrou == 1:
        return True

    else:
        return False


def attArquivo(dados, arquivo='id', pasta='user'):
    """
    Atualiza o arquivo apagando o que tinha e colocando novo texto.
    :param dados: Informações a ser atualizadas.
    :param arquivo: Nome do arquivo que deseja atulizar.
    :param pasta: Nome da pasta onde o arquivo está.
    :return: None
    """
    with open(f'{pasta}//{arquivo}.txt', 'w') as att:
        att.writelines(f'{dados}')


if __name__ == '__main__':
    print(arquivoExiste('user'))
