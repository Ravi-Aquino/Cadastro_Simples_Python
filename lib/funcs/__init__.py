def leiaInt(msg):
    """
    Docstring for leiaInt
    
    :param msg: Recebe o texto de input
    :return: retorna o número digitado pelo usuário
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor digite corretamente!\033[0m')
        except KeyboardInterrupt:
            print('\033[32mERRO! O usuário preferiu não digitar esse valor.\033[0m')
            return 3
        else:
            return n
            

def arquivoExiste(nome):
    """
    Docstring for arquivoExiste
    
    :param nome: Nome do arquivo que ira ser verificado
    :return: True se exister, False se não existir
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    Docstring for criarArquivo
    
    :param nome: Nome do arquivo a ser criado
    :return: True se tudo der certo na criação do arquivo
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        return True