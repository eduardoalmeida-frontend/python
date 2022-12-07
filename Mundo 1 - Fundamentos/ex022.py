# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúculas;
# O nome com todas minúsculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
quebra = nome.split()
qty_let = len(''.join(quebra))
# resolução alternativa: qty_let = len(nome) - nome.count(' ')
qty_let_primeiro_nome = len(quebra[0])
# resolução alternativa: qty_let_primeiro_nome = nome.find(' ')

print(f'Em maiúsculas: {maiuscula}')
print(f'Em minúsculas: {minuscula}')
print(f'Quantidade total de letras: {qty_let}')
print(f'Quantidade de letras do primeiro nome: {qty_let_primeiro_nome}')