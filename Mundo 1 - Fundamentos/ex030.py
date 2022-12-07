# Crie um programa que leia um número inteiro.
# Mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep
num = int(input('Digite um número inteiro: '))
print('PROCESSANDO...')
sleep(2)
if num % 2 == 0:
    print(f'{num} é um número par.')
else:
    print(f'{num} é um número ímpar.')