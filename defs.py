from cadastro import Cadastro
from os import system, name

def pula_linha():
    print('')

def menu():
    terminal_limpo()
    titulo = '\33[4;97mBANCO SHPC\33[m'
    print('*' * 45)
    print('*' + ' ' * 43 + '*')
    print('*' + titulo.center(53) + '*')
    print('*' + ' ' * 43 + '*')
    print('*' * 45)
    print('''
\33[1;91m|\33[m ===== \33[1;49;93m>>>>>\33[m       MENU        \33[1;49;93m<<<<<\33[m ===== \33[1;91m|\33[m
\33[1;91m|\33[m                                           \33[1;91m|\33[m
\33[1;91m|\33[m == \33[1;49;93m>>\33[m 1 \33[1;49;93m<<\33[m == \33[5;49;93m   CADASTRO                \33[m \33[1;91m|\33[m
\33[1;91m|\33[m == \33[1;49;93m>>\33[m 2 \33[1;49;93m<<\33[m == \33[5;49;93m   TRANSAÇÕES              \33[m \33[1;91m|\33[m
\33[1;91m|\33[m == \33[1;49;93m>>\33[m 0 \33[1;49;93m<<\33[m == \33[5;49;93m   SAIR                    \33[m \33[1;91m|\33[m
    ''')
    print('*' * 45)
    pula_linha()
    x = input('\33[7;49;96mOPÇÃO:\33[m ')
    return x

def terminal_limpo():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def cadastro():
    terminal_limpo()
    titulo = '\33[5;97mCADASTRO\33[m'
    print('*' * 45)
    print('*' + ' ' * 43 + '*')
    print('*' + titulo.center(53) + '*')
    print('*' + ' ' * 43 + '*')
    print('*' * 45)
    print('''
\33[1;91m|\33[m ===== \33[1;49;93m>>>>>\33[m      CADASTRO     \33[1;49;93m<<<<<\33[m ===== \33[1;91m|\33[m
\33[1;91m|\33[m                                           \33[1;91m|\33[m
\33[1;91m|\33[m == \33[1;49;93m>>\33[m 1 \33[1;49;93m<<\33[m == \33[5;49;93m   NOVO USUARIO            \33[m \33[1;91m|\33[m
\33[1;91m|\33[m == \33[1;49;93m>>\33[m 2 \33[1;49;93m<<\33[m == \33[5;49;93m   CONSULTAR USUARIO       \33[m \33[1;91m|\33[m
\33[1;91m|\33[m == \33[1;49;93m>>\33[m 0 \33[1;49;93m<<\33[m == \33[5;49;93m   RETORNAR MENU PRINCIPAL \33[m \33[1;91m|\33[m
        ''')
    print('*' * 45)
    pula_linha()
    x = input('\33[7;49;96mOPÇÃO:\33[m ')
    return x

def novo_usuario():
    usuario = Cadastro()
    print(usuario.dados)
    print('''
DESEJA ARMAZENAR OS DADOS?
1 - SIM
2 - NÃO
    ''')
    x = input('\33[7;49;96mOPÇÃO:\33[m ')
    return x

def transacoes():
    terminal_limpo()
    titulo = '\33[5;97mTRANSAÇÕES\33[m'
    print('*' * 45)
    print('*' + ' ' * 43 + '*')
    print('*' + titulo.center(53) + '*')
    print('*' + ' ' * 43 + '*')
    print('*' * 45)
    print('''
\33[1;91m|\33[m ===== \33[1;49;93m>>>>>\33[m    EM DESENVOLVIMENTO    \33[1;49;93m<<<<<\33[m ===== \33[1;91m|\33[m
    ''')