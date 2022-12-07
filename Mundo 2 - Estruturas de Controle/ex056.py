# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: 
# a média de idade do grupo;
# qual é o nome do homem mais velho;
# quantas mulheres têm menos de 20 anos.
idades = 0
mais_velho = 0
nome_mais_velho = ''
menos_20 = 0
for c in range(1, 5):
    print(f'\n----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    idades += idade
    sexo = str(input('Sexo [M/F]: ')).strip()
    if sexo.upper() == 'M':
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
    else:
        if idade < 20:
            menos_20 += 1

media = idades / 4
print(f'\nMédia de idade do grupo: {media} anos')
print(f'Nome do homem mais velho: {nome_mais_velho} | {mais_velho} anos')
print(f'Quantidade de mulheres com menos de 20 anos: {menos_20}')