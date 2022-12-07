# Crie um programa que vai gerar cinco números aleatórios e colocar em um tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numbers = (randint(1, 10), 
           randint(1, 10), 
           randint(1, 10), 
           randint(1, 10), 
           randint(1, 10))
maior = 0
menor = 0
qty = 0

print('Os números sorteados foram: ', end='')
for num in numbers:
    print(num, end=' ')
    '''if qty == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    qty += 1'''
print(f'\nO maior valor sorteado foi {max(numbers)}')
print(f'O menor valor sorteado foi {min(numbers)}')