# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA.
# Mostre os 10 primeiros termos da progressão usando a estrutura while.
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
PA = primeiro_termo
termo = 1
while termo <= 10:
        print(f'{PA} ->', end=' ')
        PA += razao
        termo += 1
print('\033[1;31mFIM!\033[m')