# Desenvolva um programa que leia seis números inteiros.
# Mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for c in range(0, 6):
    num = int(input(f'Digite o {c + 1}º número: '))
    if num % 2 == 0:
        soma += num
print(f'Soma dos números pares: {soma}')