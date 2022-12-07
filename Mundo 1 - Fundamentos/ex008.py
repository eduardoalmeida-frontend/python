# Escreva um programa que leia um valor em metros.
# Exiba convertido em kms, hectometros, decâmetros, decimetros, centímetros e milímetros.
m = float(input('Digite uma distância em metros: '))
print(f'Em kilômetros: {m / 1000:.0f} kms \nEm hectômetros: {m / 100:.0f} hms' +
f'\nEm decâmetros: {m / 10:.0f} dam \nEm decímetros: {m * 10:.0f} dm' + 
f'\nEm centímetros: {m * 100 :.0f} cms \nEm milímetros: {m * 1000:.0f} mms.')