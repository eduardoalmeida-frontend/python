# Refaça o DESAFIO 035 dos triângulos.
# Acrescente o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais;
# Isósceles: dois lados iguais;
# Escaleno: todos os lados diferentes.
from time import sleep
print('-=' * 20)
print(' ' * 7 + 'Analisador de Triângulos')
print('-=' * 20)
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
order = [reta1, reta2, reta3]
order.sort()
print('PROCESSANDO...')
sleep(2)
if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('É possível formar um triângulo com as retas indicadas.')
    if reta1 == reta2 == reta3:
        print('Tipo: triângulo equilátero.')
    elif (reta1 == reta2 != reta3 != reta1):
        print('Tipo: triângulo isósceles.')
    else:
        print('Tipo: triângulo escaleno.')
else:
    print('Não é possível formar um triângulo com as retas indicadas.')