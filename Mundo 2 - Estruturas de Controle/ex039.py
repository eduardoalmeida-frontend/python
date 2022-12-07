# Faça um programa que leia o ano de nascimento de um jovem.
# Informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

curr_year = date.today().year
born = int(input('Ano de nascimento: '))
print('\n1 - Masculino \n2 - Feminino \n3 - Outro')
gender = int(input('Informe seu sexo com base no menu acima: '))
age = curr_year - born
print(f'\nQuem nasceu em {born} tem {age} anos em {curr_year}.')

if gender != 1:
    print('Você não precisa se alistar.\n')
else:
    if age > 18:
        print(f'''Você já deveria ter se alistado há {age - 18} ano(s).
Seu alistamento foi em {curr_year - (age - 18)}.\n''')
    elif age < 18:
        print(f'''Ainda faltam {18 - age} ano(s) para seu alistamento.
Seu alistamento será em {(18 - age) + curr_year}.\n''')
    else:
        print(f'Você deve se alistar \033[1;31;40mimediatamente\033[m.\n')