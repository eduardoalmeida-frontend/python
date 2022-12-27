# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = str(input('Digite uma expressão: '))
parenteses_abertura = expression.count('(')
parenteses_fechamento = expression.count(')')

if parenteses_abertura == parenteses_fechamento:
    print('Expressão válida.')
else:
    print('Expressão inválida.')