# Crie um programa que leia o nome de uma cidade.
# Diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome de uma cidade: ')).strip()
if (cidade[:5].upper()) == 'SANTO':
    print('O nome dessa cidade começa com Santo.')
else:
    print('O nome dessa cidade não começa com Santo.')