# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('\033[1;31;40mDigite um número para obter sua tabuada:\033[m '))
print('-' * 13)
for c in range(1, 11):
    print(f'{n:2} x {c:2} = {n * c:2}')
print('-' * 13)