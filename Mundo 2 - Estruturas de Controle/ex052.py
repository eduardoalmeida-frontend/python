# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
divisoes = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[33m{i}\033[m', end=' ')
        divisoes += 1
    else:
        print(f'\033[31m{i}\033[m', end=' ')

print(f'\n\033[mO número {num} foi divisível {divisoes} vezes.')

if divisoes == 2:
    print('E, por isso, ele É PRIMO!')
else:
    print('E, por isso, ele NÃO É PRIMO!')