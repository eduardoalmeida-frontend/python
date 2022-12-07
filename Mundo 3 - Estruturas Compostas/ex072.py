# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
                       'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                       'dezenovo', 'vinte')
op = 'S'
while op.upper() == 'S':
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número \033[1;31m{numeros_por_extenso[num]}\033[m.')
        op = str(input('Deseja continuar [S/N]? '))
    else:
        print('Tente novamente. ', end='')