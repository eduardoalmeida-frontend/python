# Escreva um programa que leia um número inteiro qualquer.
# Peça para o usuário escolher qual será a base de conversão:
# Binário;
# Octal;
# Hexadecimal.
num = int(input('Digite um número: '))
print('\n1 - Binário \n2 - Octal \n3 - Hexadecimal\n')
base = int(input('Escolha uma base conforme o menu acima: '))

if base == 1:
    print(f'Número convertido para binário: {bin(num)[2:]}\n')
elif base == 2:
    print(f'Número convertido para octal: {oct(num)[2:]}\n')
elif base == 3:
    print(f'Número convertido para hexadecimal: {hex(num)[2:]}\n')
else:
    print('Opção inválida.')