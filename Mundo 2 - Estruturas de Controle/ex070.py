# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de 1000.
# C) Qual é o nome do produto mais barato.
total = mais1000 = preco_mais_barato = qty = 0
nome_mais_barato = ''
print('-' * 35)
print('        LOJA SUPER BARATÃO        ')
print('-' * 35)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    qty += 1
    if preco > 1000:
        mais1000 += 1
    if qty == 1 or preco < preco_mais_barato:
        nome_mais_barato = nome
        preco_mais_barato = preco
    op = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    while op not in 'S' or 'N':
        op = str(input('Opção inválida. Quer continuar [S/N]? ')).upper().strip()[0]
    if op == 'N':
        print('---------- FIM DO PROGRAMA -----------')
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R$ {preco_mais_barato:.2f}')