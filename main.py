from lib.interface.__init__ import *
from lib.funcs.__init__ import *
from time import sleep


arq = r'arquivo\Repositório.txt'
if arquivoExiste(arq):
    print(f'Arquivo de Repositório encontrado')
else:
    criarArquivo(arq)
    
# Opções que aparecerão para o usuário escolher
opções = ['Ver Pessoas cadastradas','Cadastrar nova Pessoa','Remover uma Pessoa','Alterar uma Pessoa', 'Sair do Sistema']
menu(opções)

while True:
    escolha = leiaInt('Sua opção: ')
    
    if escolha == 1:
        cabeçalho('VER PESSOAS CADASTRADAS')
        print(f'{"POS.":<7}{"ID":<5}{"NOME":^25}{"IDADE":>3}')
        print('-'*50)
        lerArquivo(arq)
        sleep(1)
        menu(opções)
        
    elif escolha == 2:
        while True:
            cabeçalho('CADASTRAR NOVA PESSOA')
            nome = str(input('Nome: ')).capitalize().strip()
            idade = leiaInt('Idade: ')
            idPessoa = geradorId(arq)
            cadastrar(arq,idPessoa,nome,idade)
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
            
            while resp not in 'SN':
                resp = str(input('Digite corretamente. Quer continuar? [S/N] ')).upper().strip()[0]
            if resp == 'N':
                break
            
        sleep(0.5)
        menu(opções)
        
    elif escolha == 3:
        
        cabeçalho("REMOVER INDIVÍDUO")
        ações = ['Deletar por ID', 'Deletar por posição']
        menu(ações)
        while True:
                opc = leiaInt('Sua opção: ')
                
                if opc == 1:
                    cod = leiaInt('Digite o Id de quem você deseja remover: ')
                    deletarId(arq,cod)
                    break
                elif opc == 2:
                    cod = leiaInt('Digite a posição de quem você deseja remover: ')
                    deletarPos(arq,cod)
                    break
                else:
                    print('\033[31mERRO! Digite uma opção válida!\033[0m')
                    menu(ações)
                    
        sleep(0.5)
        menu(opções)
        
    elif escolha == 4:
        cabeçalho("ALTERANDO UMA PESSOA")
        print(f'{"POS.":<7}{"ID":<5}{"NOME":^25}{"IDADE":>3}')
        print('-'*50)
        lerArquivo(arq)
        
        cod = leiaInt('Id da pessoa a ser atualizada: ')
        ações = ['Alterar Nome', 'Alterar idade']
        menu(ações)
        opc = leiaInt("\033[33mSua opção: \033[0m")
        
        if opc == 1:
            novoNome = str(input("\033[35mNovo nome: \033[0m")).strip().capitalize()
            
            if novoNome == '':
                novoNome = "<Desconhecido>"
                
            atualizarNome(arq, cod, novoNome)
            sleep(1)
            menu(opções)
            
        elif opc == 2:
            novaIdade = leiaInt("Nova idade: ")
            
            if novaIdade == None:
                novaIdade = 0
                
            atualizarIdade(arq,cod, novaIdade)
            sleep(1)
            menu(opções)       
    elif escolha == 5:
        cabeçalho('ENCERRANDO O PROGRAMA')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[0m')
   