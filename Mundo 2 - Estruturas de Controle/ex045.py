# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''0 - Pedra
1 - Papel
2 - Tesoura''')
jog = int(input('Digite sua jogada com base nas opções acima: '))

print('\nJO')
sleep(1.5)
print('KEN')
sleep(1.5)
print('PO!!!\n')
sleep(1.5)

print('\033[1;35m-=\033[m' * 10)
print(f'Computador: {itens[comp]}')
print(f'Jogador: {itens[jog]}')
print('\033[1;35m-=\033[m' * 10)
print('')

if comp == 0: # computador jogou PEDRA
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('JOGADOR VENCE!')
    elif jog == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Opção inválida.')

elif comp == 1: # computador jogou PAPEL
    if jog == 0:
        print('COMPUTADOR VENCE!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('JOGADOR VENCE!')
    else:
        print('Opção inválida.')

elif comp == 2: # computador jogou TESOURA
    if jog == 0:
        print('JOGADOR VENCE!')
    elif jog == 1:
        print('COMPUTADOR VENCE!')
    elif jog == 2:
        print('EMPATE!')
    else:
        print('Opção inválida.')
print('')