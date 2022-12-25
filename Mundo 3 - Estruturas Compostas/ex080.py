# Crie um programa onde o usuário possa digitar cinco valores númericos.
# Cadastre-os em uma lista, já na posição correta de inserção (sem usasr o sort()).
# No final, mostre a lista ordenada na tela.
lista = []

for i in range(0, 5):
    if len(lista) == 0:
        lista.append(int(input('Digite um valor: ')))
        print('Adicionado ao final da lista...')
    else:
        num = int(input('Digite um valor: '))
        for i in range(0, len(lista)):
            if num > max(lista):
                lista.insert(-1, num)
                print('Adicionado ao final da lista...')
            if num < min(lista):
                lista.insert(0, num)
                print('Adicionado na posição 0 da lista...')
print('-=' * 30)

print(f'Os valores digitados em ordem foram {lista}')