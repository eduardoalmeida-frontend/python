# Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
# Calcule seu IMC e mostree seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso;
# Entre 18.5 e 25: Peso ideal;
# Entre 25 e 30: Sobrepeso;
# Entre 30 e 40: Obesidade;
# Acima de 40: Obesidade mórbida.
peso = float(input('Digite seu peso (kg): '))
alt = float(input('Digite sua altura (m): '))
imc = peso / (alt ** 2)
print(f'Seu IMC é: \033[1;31;40m{imc:.1f}\033[m')

if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está na faixa de peso ideal.')
elif 25 <= imc < 30:
    print('Você está em sobrepeso.')
elif 30 <= imc < 40:
    print('Você está em obesidade.')
else:
    print('Você está em obesidade mórbida. Cuidado!')