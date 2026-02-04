from lib.interface.__init__ import *
from lib.funcs.__init__ import *
from time import sleep

arq = r'arquivo\Repositório.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')
    
criarArquivo(arq)
opções = ['Ver Pessoas cadastradas','Cadastrar nova Pessoa', 'Sair do Sistema']
menu(opções)
while True:
    escolha = leiaInt('Sua opção: ')
    if escolha == 1:
        cabeçalho('VER PESSOAS CADASTRADAS')
        sleep(1)
        menu(opções)
    elif escolha == 2:
        cabeçalho('CADASTRAR NOVA PESSOA')
        sleep(1)
        menu(opções)
    elif escolha == 3:
        cabeçalho('ENCERRANDO O PROGRAMA')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[0m')
   