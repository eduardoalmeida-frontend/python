# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 37)
    if num < 0:
        break
    for c in range(1, 11):
            produto = num * c
            print(f'{num:2} x {c:2} = {produto:2}')
    print('-' * 37)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')