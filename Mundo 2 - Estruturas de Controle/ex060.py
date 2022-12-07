# Faça um programa que leia um número qualquer e mostre o seu fatorial (while e for).
num = int(input('Digite um número para obter seu fatorial: '))
c = num
f = 1
print(f'{num}! =', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f'{f}')

'''num = int(input('Digite um número para obter seu fatorial: '))
c = 1
fat = 1
while c <= num:
    fat *= c
    c += 1
print(f'{num}! = {fat}')'''

'''num = int(input('Digite um número para obter seu fatorial: '))
fat = 1
for c in range(1, num + 1):
    fat *= c
print(f'{num}! = {fat}')'''