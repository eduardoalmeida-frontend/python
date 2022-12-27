# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
op = 'S'

while True:
    if op.upper() == 'S':
        num = int(input('Digite um valor: '))
        if num in lista:
            print('Valor duplicado! Não vou adicionar...')
            op = str(input('Quer continuar? [S/N] '))
            while op.upper() not in 'SN':
                op = str(input('Opção inválida. Quer continuar? [S/N] '))
        else:
            lista.append(num)
            print('Valor adicionado com sucesso...')
            op = str(input('Quer continuar? [S/N] '))
            while op.upper() not in 'SN':
                op = str(input('Opção inválida. Quer continuar? [S/N] '))
    else:
        break

print('-=' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')