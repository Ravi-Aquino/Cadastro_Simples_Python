
from time import sleep
def cabeçalho(msg):
    print('-'*50)
    print(f'\033[32m{msg:^50}\033[0m')
    print('-'*50)
    
    
def menu(lst):
    cabeçalho('MENU')
    for i, v in enumerate(lst):
        print(f'\033[36m{i + 1}\033[0m - \033[34m{v}\033[0m')
        sleep(0.1)
        