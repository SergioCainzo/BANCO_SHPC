from cadastro import Cadastro
from time import sleep
import defs



escolha = defs.menu()

while True:
    if escolha == '1':
        sleep(0.3)
        defs.novo_usuario()
        break
    elif escolha == '2':
        sleep(0.3)
        break
    elif escolha == '0':
        print('''
\33[1;91m|\33[m ===== \33[1;49;93m>>>>>\33[m SAINDO DO SISTEMA \33[1;49;93m<<<<<\33[m ===== \33[1;91m|\33[m
        ''')
        break
    else:
        print('''
\33[1;91m|\33[m ===== \33[1;49;93m>>>>>\33[m  OPÇÃO  INVÁLIDA  \33[1;49;93m<<<<<\33[m ===== \33[1;91m|\33[m
''')
        sleep(0.5)
        defs.terminal_limpo()
        sleep(1)
        escolha = defs.menu()