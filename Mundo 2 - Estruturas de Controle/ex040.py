# Crie um programa que leia duas notas de um aluno e calcule sua média.
# Mostre uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: reprovado;
# Média entre 5.0 e 6.9: recuperação;
# Média 7.0 ou superior: aprovado.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'\nSua média é: {m:.1f}')

if m < 5:
    print('Você está \033[1;31mreprovado\033[m.\n')
elif 7 > m >= 5: # denotação simplificada para testes lógicos
    print('Você está de \033[1;33mrecuperação\033[m.\n')
else:
    print('Você está \033[1;32maprovado\033[m.\n')