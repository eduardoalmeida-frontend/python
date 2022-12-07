# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira.
# Mostre quantos dólares ela pode comprar.
# Considere: US$ 1.00 = R$ 3.27
real = float(input('Quanto dinheiro você tem na carteira: R$ '))
dolar = real / 5.17
euro = real / 5.15
iene = real * 27.12
print((f'Com R$ {real:.2f}, você pode comprar aproximadamente US$ {dolar:.2f}, ' + 
f'€ {euro:.2f} ou ¥ {iene:.2f}'))