# Faça um programa que leia um número de 0 a 9999.
# Mostre na tela cada um dos dígitos separados.
# Fazer como string e matematicamente.
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

'''tamanho = len(num)
if tamanho == 4:
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')
elif tamanho == 3:
    print(f'Unidade: {num[2]}')
    print(f'Dezena: {num[1]}')
    print(f'Centena: {num[0]}')
elif tamanho == 2:
    print(f'Unidade: {num[1]}')
    print(f'Dezena: {num[0]}')
else:
    print(f'Unidade: {num[0]}')'''