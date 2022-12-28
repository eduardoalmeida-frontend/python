# Crie um programa onde o usuário possa digitar sete valores númericos.
# Cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
for i in range(0, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        numeros[0].append(num) # pares
    else:
        numeros[1].append(num) # ímpares

numeros[0].sort()
print(f'Pares: {numeros[0]}')
numeros[1].sort()
print(f'Ímpares: {numeros[1]}')