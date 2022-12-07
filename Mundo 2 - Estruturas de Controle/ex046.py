# Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artifício.
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;31mBOOM!\033[m')