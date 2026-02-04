from lib.interface.__init__ import *
from lib.funcs.__init__ import *
from time import sleep
import random
arq = r'arquivo\Repositório.txt'
if arquivoExiste(arq):
    print(f'Arquivo de Repositório encontrado')
else:
    criarArquivo(arq)
opções = ['Ver Pessoas cadastradas','Cadastrar nova Pessoa','Remover indivíduo', 'Sair do Sistema']
menu(opções)
while True:
    escolha = leiaInt('Sua opção: ')
    if escolha == 1:
        cabeçalho('VER PESSOAS CADASTRADAS')
        lerArquivo(arq)
        sleep(1)
        menu(opções)
    elif escolha == 2:
        while True:
            cabeçalho('CADASTRAR NOVA PESSOA')
            nome = str(input('Nome: ')).capitalize().strip()
            idade = leiaInt('Idade: ')
            idPessoa = random.randint(1,100)
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
        cod = leiaInt('Digite o Id de quem você deseja remover')
        deletar(arq,cod)
    elif escolha == 4:
        cabeçalho('ENCERRANDO O PROGRAMA')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[0m')
   