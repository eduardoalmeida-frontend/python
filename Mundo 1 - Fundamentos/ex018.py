# Faça um programa que leia um ângulo qualquer.
# Mostre na tela o valor do seno, cosseno e tangente desse ângulo utilizando módulos.
from math import sin, cos, tan, radians

ang = int(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'Ângulo: {ang}° \nSeno: {sen:.2f} \nCosseno: {cos:.2f} \nTangente: {tan:.2f}')