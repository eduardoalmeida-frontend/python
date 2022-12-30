# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) quantas pessoas foram cadastradas;
# b) uma listagem com as pessoas mais pesadas;
# c) uma listagem com as pessoas mais leves.
pessoa = list()
pessoas = list()
maior_peso = menor_peso = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]
        if pessoa[1] < menor_peso:
            menor_peso = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N] '))
    while resp.upper() not in 'SN':
        resp = str(input('Opção inválida. Quer continuar? [S/N] '))
    if resp.upper() == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {maior_peso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {menor_peso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')