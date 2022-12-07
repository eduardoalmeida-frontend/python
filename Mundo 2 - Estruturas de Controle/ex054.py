# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    born = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    idade = ano_atual - born
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'\nQuantidade de maiores de idade: {maior}')
print(f'Quantidade de menores de idade: {menor}')