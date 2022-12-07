# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem: 
# Cobrando R$ 0.50 por km para viagens de até 200km;
# Cobrando R$ 0.45 para viagens mais longas.
from time import sleep
dist = int(input('Digite a distância da viagem (km): '))
print('PROCESSANDO...')
sleep(2)
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f'Preço da passagem: R$ {preco:.2f}')

'''if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print(f'Preço da passagem: R$ {preco:.2f}')'''