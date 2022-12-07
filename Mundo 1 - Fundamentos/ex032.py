# Faça um programa que leia um ano qualquer 
# Mostre se ele é BISSEXTO.
from datetime import date
from time import sleep
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
print('PROCESSANDO...')
sleep(2)
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')