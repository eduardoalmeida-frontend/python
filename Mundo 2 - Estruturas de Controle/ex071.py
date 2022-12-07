# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro).
# O programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1.
cinq = vinte = dez = um = 0
print('=' * 29)
print('          BANCO CEV           ')
print('=' * 29)
while True:
    valor = float(input('Que valor você quer sacar? R$ '))
    if valor >= 50:
        cinq = valor // 50
        valor %= 50
        print(f'Total de {cinq} cédulas de R$ 50')
    
    if valor >= 20:
        vinte = valor // 20
        valor %= 20
        print(f'Total de {vinte} cédulas de R$ 20')

    if valor >= 10:
        dez = valor // 10
        valor %= 10
        print(f'Total de {dez} cédulas de R$ 10')
    
    if valor >= 1:
        um = valor // 1
        valor %= 1
        print(f'Total de {um} cédulas de R$ 1')

    if valor == 0:
        print('=' * 29)
        break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')