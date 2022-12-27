# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
op = 'S'

while True:
    if op.upper() == 'S':
        num = int(input('Digite um valor: '))
        lista.append(num)
    else:
        break
    op = str(input('Quer continuar? [S/N] '))
    while op.upper() not in 'SN':
        op = str(input('Opção inválida. Quer continuar? [S/N] '))

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')