# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar:
# O valor da casa;
# O salário do comprador;
# Em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal:
# Ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prest = valor / (anos * 12)

if prest > (sal - (sal * (30 / 100))):
    print('Empréstimo negado! O valor da prestação excede 30% do seu salário.')
else:
    print(f'Empréstimo aprovado! Valor da prestação mensal: R$ {prest:.2f} ')