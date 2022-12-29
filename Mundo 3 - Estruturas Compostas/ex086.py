# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], [], [], [], [], [], [], []]
for linha in range(0, 2):
    for coluna in range(0, 2):
        matriz[linha][coluna] = int(input('Digite um valor: '))

for i in matriz:
    print(f'[ {i} ]', end=' ')