# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
maior = homem = mulher_menor_20 = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA   ')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Opção inválida. Sexo [M/F]: ')).upper().strip()[0]
    print('-' * 25)
    if idade > 18:
        maior +=1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menor_20 += 1
    op = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Opção inválida. Quer continuar [S/N]? ')).upper().strip()[0]
    if op == 'N':
        print('====== FIM DO PROGRAMA ======')
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher_menor_20} mulheres com menos de 20 anos.')