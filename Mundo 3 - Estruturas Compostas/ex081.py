# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) quantos números foram digitados;
# B) a lista de valores, ordenada de forma decrescente;
# C) se o valor 5 foi digitado e está ou não na lista.

lista = []
qty = 0
op = 'S'

while True:
    if op.upper() == 'S':
        lista.append(int(input('Digite um valor: ')))
        qty += 1
        op = str(input('Quer continuar? [S/N] '))
        while op.upper() not in 'SN':
            op = str(input('Opção inválida. Quer continuar? [S/N] '))
    else:
        break

print('-=' * 30)

print(f'Você digitou {qty} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')