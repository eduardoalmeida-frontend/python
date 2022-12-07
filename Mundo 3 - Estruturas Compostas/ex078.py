# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
print('=-' * 30)

print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for pos, num in enumerate(lista):
    if num == max(lista):
        print(f'{pos}... ', end='')

print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for pos, num in enumerate(lista):
    if num == min(lista):
        print(f'{pos}... ', end='')