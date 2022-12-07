# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = qty = soma = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 p/ sair]: '))
    if n != 999:
        qty += 1
        soma += n

print(f'\nQuantidade de número digitados: {qty}')
print(f'Soma dos números digitados: {soma}\n')