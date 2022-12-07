# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo.
# Calcule e mostre o comprimento da hipotenusa utilizando módulos.
from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'Hipotenusa: {float(hypot(co, ca)):.2f}')