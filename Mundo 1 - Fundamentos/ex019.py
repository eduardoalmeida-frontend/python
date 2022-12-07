# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o escolhido utilizando módulos.
from random import choice

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
sorteio = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido para apagar o quadro foi o (a): {choice(sorteio)}.')