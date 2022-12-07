# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois, mostre:
# A) Apenas os 5 primeiros colocados;
# B) Os últimos 4 colocados da tabela;
# C) Uma lista com os times em ordem alfabética;
# D) Em que posição na tabela está o time da Chapecoense.
tabela_campeonato_brasileiro = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athetico-PR',
                                'Atlético-MG', 'Botafogo', 'América-MG', 'Fortaleza', 'São Paulo', 'Santos', 'Goiás', 
                                'Bragantino', 'Coritiba', 'Atlético-GO', 'Ceará SC', 'Avaí', 'Juventude')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {tabela_campeonato_brasileiro}')
print('-=' * 15)

print(f'Os 5 primeiros são {tabela_campeonato_brasileiro[:5]}')
print('-=' * 15)

print(f'Os 4 últimos são {tabela_campeonato_brasileiro[-4:]}')
print('-=' * 15)

print(f'Times em ordem alfabética: {sorted(tabela_campeonato_brasileiro)}')
print('-=' * 15)

if 'Chapecoense' in tabela_campeonato_brasileiro:
    print(f'O Chapecoense está na {tabela_campeonato_brasileiro.index("Chapecoense")}ª posição.')
else:
    print(f'O Chapecoense não está disputando a Série A esse ano.')