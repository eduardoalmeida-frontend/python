# Escreva uma programa que pergunte o salário de um funcionário.
# Calcule o valor do seu aumento.
# Para salários superiores a R$ 1250.00, calcule um aumento de 10%;
# Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep
sal = float(input('Digite o salário do funcionário: R$ '))
print('PROCESSANDO...')
sleep(2)
if sal > 1250:
    novo_sal = sal + (sal * (10 / 100))
else:
    novo_sal = sal + (sal * (15 / 100))
print(f'Novo salário: R$ {novo_sal:.2f}')