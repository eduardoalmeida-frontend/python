# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
while True:
    numuser = int(input('Diga um valor: '))
    numpc = randint(0, 10)
    res = numuser + numpc
    if res % 2 == 0:
        opres = 'PAR'
    else:
        opres = 'IMPAR'
    opuser = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    while opuser not in 'PI':
        opuser = str(input('Opção inválida. Par ou ímpar [P/I]? ')).strip().upper()[0]
    print('-' * 30)
    print(f'Você jogou {numuser} e o computador {numpc}. Total de {res} DEU {opres}')
    print('-' * 30)
    if opuser == opres[0]:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
        vitorias += 1
    else:
        print('Você PERDEU!')
        print('=-' * 15)
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')