# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Cada litro de tinta pinta uma área de 2m².
larg = float(input('Digite a largura da parede (m): '))
alt = float(input('Digite a altura da parede (m): '))
area = larg * alt
tinta = area / 2
print(f'Dimensões da parede: {larg:.2f}x{alt:.2f} \nÁrea da parede: {area} m²'
f'\nQuantidade de tinta necessária para pintá-la: {tinta:.2f}L')