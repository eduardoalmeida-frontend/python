# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
op = 'S'
soma = qty = maior = menor = 0
while op.upper() == 'S':
    num = int(input('Digite um número: '))
    soma += num
    qty += 1
    if qty == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    op = str(input('Deseja continuar [S/N]? '))
    while op.upper() not in 'SN':
        op = str(input('Opção inválida. Deseja continuar [S/N]? '))

media = soma / qty
print(f'\nQuantidade de números digitados: {qty} \nMédia dos números digitados: {media:.2f} \nMaior valor: {maior} \nMenor valor: {menor}')