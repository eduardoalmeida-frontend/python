# Faça um programa que leia três números.
# Mostre qual é o maior e qual é o menor.
from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# Verificando quem é o menor
menor = num1
print('PROCESSANDO...')
sleep(2)
if (num2 < num1) and (num2 < num3):
    menor = num2
if (num3 < num1) and (num3 < num2):
    menor = num3
# Verificando quem é o maior
maior = num1
if (num2 > num1) and (num2 > num3):
    maior = num2
if (num3 > num1) and (num3 > num2):
    maior = num3
print(f'Menor número: {menor}')
print(f'Maior número: {maior}')