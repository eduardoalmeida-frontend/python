# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], [], [], [], [], [], [], []]

for i in range(0, 9):
        matriz[i] = int(input(f'Digite um valor: '))

print('-=' * 30)
for pos, i in enumerate(matriz):
    if (pos + 1) % 3 == 0:
        print(f'[  {i}  ]')    
    else: 
        print(f'[  {i}  ]', end=' ')