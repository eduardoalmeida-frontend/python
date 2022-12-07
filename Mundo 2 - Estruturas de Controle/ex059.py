# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n = 0
while n != 5:
    print('\033[1;33m-=-\033[m' * 7)
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa')
    n = int(input('Escolha uma opção: '))
    print('\033[1;33m-=-\033[m' * 7)
    if n == 1:
        soma = n1 + n2
        print(f'\n{n1} + {n2} = {soma}\n')
    elif n == 2:
        produto = n1 * n2
        print(f'\n{n1} x {n2} = {produto}\n')
    elif n == 3:
        if n1 > n2:
            print(f'\nMaior número: {n1}\n')
        elif n2 > n1:
            print(f'\nMaior número: {n2}\n')
        else:
            print('\nOs números são iguais.\n')
    elif n == 4:
        n1 = int(input('\nDigite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif n == 5:
        print('Finalizando...')
        print('\033[1;33m-=-\033[m' * 7)
    else:
        print('Opção inválida. Tente novamente!')
    sleep(2)

print('\nFIM DO PROGRAMA!\n')