
class Cadastro:

    def __init__(self):
        print('''
\33[1;91m|\33[m ===== \33[1;49;93m>>>>>\33[m      CADASTRO     \33[1;49;93m<<<<<\33[m ===== \33[1;91m|\33[m
        ''')
        self._nome = input('NOME COMPLETO: ').title()
        self._idade = int(input('IDADE: '))


    @property
    def dados(self):
        return f'''
\33[1;91m|\33[m ===== \33[1;49;93m>>>>>\33[m DADOS DO USUÁRIO \33[1;49;93m<<<<<\33[m ===== \33[1;91m|\33[m
\33[1;91m|\33[m\33[7;49;96mNOME\33[m: {self._nome}
\33[1;91m|\33[m\33[7;49;96mIDADE\33[m: {self._idade}
'''
