# A Confederação Nacional de Natação precisa um programa que:
# Leia o ano de nascimento de um atleta;
# Mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim;
# Até 14 anos: Infantil;
# Até 19 anos: Junior;
# Até 25 anos: Sênior;
# Acima: Master.
from datetime import date

curr_year = date.today().year
born = int(input('Digite o ano em que você nasceu: '))
age = curr_year - born
print(f'\nO atleta tem {age} anos.')

if age <= 9:
    print('Categoria: mirim.\n')
elif age <= 14:
    print('Categoria: infantil.\n')
elif age <= 19:
    print('Categoria: junior.\n')
elif age <= 25:
    print('Categoria: sênior.\n')
else:
    print('Categoria: master.\n')