# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7.00 por cada km acima do limite.
vel = float(input('Digite a velocidade do carro (km): '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado! \nValor da multa: R$ {multa:.2f}')
else:
    print('Você está dentro da velocidade permitida da via.')