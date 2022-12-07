# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar advinhar até acertar.
# Mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
jogador = ''
tentativas = 0
acertou = False
print('\033[1;33m-=-\033[m' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('\033[1;33m-=-\033[m' * 20)

while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if computador > jogador:
            print('\nMais... Tente novamente!')
        else:
            print('\nMenos... Tente novamente!')

print(f'\nAcertou com {tentativas} palpites. Parabéns!\n')