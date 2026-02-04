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


def lerArquivo(nome):
    """
    Docstring for lerArquivo
    
    :param nome: Recebe o nome do arquivo a ser lido
    :return: retorna os arquivos lidos
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Falha ao ler o arquivo.')
    else:
        print(f'{"POS.":<7}{"ID":<5}{"NOME":^25}{"IDADE":>3}')
        linhas = a.readlines()
        
        for i, value in enumerate(linhas):
           partes = value.strip().split(';')
           
           if len(partes) == 3:
                id_, nome, idade = partes
                print(f'{i+1:<7}{id_:<5}{nome:^25}{idade:>3}')
    finally:
        a.close()


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
        print(f'Arquivo {nome} criado com sucesso')


def cadastrar(arq,id,nome='<Desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro na abertura do arquivo.")
    else:
        try:
            if nome == '':
                nome = '<Desconhecido>'
            a.write(f'{id};{nome};{idade}\n')
        except:
            print("Falha ao adicionar")
        else:
            print(f'Novo registro. {nome} adicionado à repositório.')
        finally:
            a.close()
            



def deletar(arq,cod):
    try:
        a = open(arq, 'rt')
        dados = a.readlines()
        a.close()
        
        for i in range(len(dados)):
            if dados[i].startswith(str(cod)):
                del dados[i]
                break
        
        a = open(arq, 'wt')
        for i in dados:
            a.write(i)
        a.close()
    except (ValueError, TypeError, IndexError):
        print("\033[31mERRO! ID não encontrado, não foi possível excluir.\033[0m")
    else:
        print(f'ID {cod} deletado com sucesso')