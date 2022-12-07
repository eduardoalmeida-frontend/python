# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
PA = primeiro_termo
termo = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while termo <= total:
            print(f'{PA} ->', end=' ')
            PA += razao
            termo += 1
    print('\033[1;31mPAUSA\033[m')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'\nProgressão finalizada com {total} termos mostrados.\n')