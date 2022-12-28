# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) quantas pessoas foram cadastradas;
# b) uma listagem com as pessoas mais pesadas;
# c) uma listagem com as pessoas mais leves.
pessoas = list()
pessoa = list()

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(str(input('Peso: ')))
    pessoas = pessoa[:]
    resp = str(input('Quer continuar? [S/N] '))
    while resp.upper() not in 'SN':
        resp = str(input('Opção inválida. Quer continuar? [S/N] '))
    if resp.upper() == 'N':
        break

# print(f'Ao todo, você cadastrou {len(pessoas) / 2} pessoas.')
print(pessoas)