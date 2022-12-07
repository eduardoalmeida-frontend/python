dia = int(input('Por quantos dias você alugou o veículo? '))
km = float(input('Quantos kms você rodou com o veículo? '))
total = (dia * 60) + (km * 0.15) 
print(f'Total a pagar: R$ {total:.2f}')