# Crie um algoritmo que leia um número.
# Mostre seu dobro, triplo e raiz quadrada.
num = int(input('Digite um número: '))
print(f'Dobro: {num * 2} \nTriplo: {num * 3} \nRaiz quadrada: {pow(num, (1 / 2)):.2f}')