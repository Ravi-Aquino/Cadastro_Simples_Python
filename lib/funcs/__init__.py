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
            raise
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
    """
    Docstring for cadastrar
    
    :param arq: Nome do arquivo onde estão os registros
    :param id: Número aleatório gerado apartir da função randomizar()
    :param nome: Nome digitado pelo usuário
    :param idade: Idade digitada pelo usuário
    """
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
            

def geradorId(arq):
    """
    Docstring for randomizar
    
    :param arq: Nome do arquivo onde estão os registros
    :return: retorna um id único entre 1 e 100

    """
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mERRO! Falha ao ler o arquvio.')
    else:
        linhas = a.readlines()
        a.close()
        
        ids_existentes = []
        novo_id = 0
        for linha in linhas:
            partes = linha.strip().split(';')
            ids_existentes.append(partes[0])
            novo_id += 1
        while True:
            if not novo_id in ids_existentes:
                return novo_id
     
        

def deletarId(arq,cod):
    """
    Docstring for deletarId
    
    :param arq: Nome do arquivo onde estão os registros
    :param cod: Id digitado pelo usuário
    """
    try:
        a = open(arq, 'rt')
        dados = a.readlines()
        a.close()
        
        encontrado = False
        
        for i in range(len(dados)):
            if dados[i].startswith(str(cod)):
                del dados[i]
                encontrado = True
                break
            
        if encontrado:
            a = open(arq, 'wt')
            for i in dados:
                a.write(i)
            a.close()
            print(f'ID {cod} deletado com sucesso')
        else:
            print(f"\033[31mERRO! Id {cod} não encontrado.\033[0m")
            
    except (ValueError, TypeError, IndexError):
        print("\033[31mERRO! Não foi possível excluir.\033[0m")
        
        
def deletarPos(arq,cod):
    """
    Docstring for deletarPos
    
    :param arq: Nome do arquivo onde estão os registros
    :param cod: Posição digitada pelo usuário
    """
    try:
        a = open(arq, 'rt')
        dados = a.readlines()
        del dados[cod - 1]
        a.close()
        
        
        a = open(arq, 'wt')
        for i in dados: 
            a.write(i)
        a.close()
                
    except (ValueError, TypeError, IndexError):
        print("\033[31mERRO! Posição não encontrada, não foi possível excluir.\033[0m")  
    else:
        print(f'\033[32mPosição {cod} deletada com sucesso!\033[0m')     
        

def atualizarNome(arq, id, nome):
    try:
        a = open(arq, 'rt')
    except:
        print('Falha ao ler o arquivo.')
    else:
        linhas = a.readlines()
        a.close()
       
        for i in range(len(linhas)):
            partes = linhas[i].strip().split(';')
            if partes[0] == str(id):
               partes[1] = nome
               linhas[i] = ';'.join(partes) + '\n'
               break
           
        a = open(arq, 'wt')
        a.writelines(linhas)
        a.close()
        print("\033[32mNome atualizado com sucesso!\033[0m")
    finally:
        try:
            a.close()
        except:
            pass
        
def atualizarIdade(arq, id, idade):
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mHouve um erro ao abrir o arquivo!\033[0m')
    else:
        linhas = a.readlines()
        a.close()
        
        for i in range(len(linhas)):
            partes = linhas[i].strip().split(';')
            if partes[0] == str(id):
                partes[2] = str(idade)
                linhas[i] = ';'.join(partes) + '\n'
                break
            
        a = open(arq, 'wt')
        a.writelines(linhas)
        a.close()
        print("\033[32mIdade atualizada com sucesso!\033[0m") 
    finally:
        try:
            a.close()
        except:
            pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          