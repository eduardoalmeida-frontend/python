# Faça um programa que leia o nome completo de uma pessoa.
# Mostre em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')
# resolução alternativa: print(f'Último nome: {nome[len(nome) - 1]}')