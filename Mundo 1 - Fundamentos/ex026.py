# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "a";
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
letra_a = frase.count('A')
primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1

print(f'Essa frase tem {letra_a} letra (s) A.')
print(f'A letra A aparece pela primeira vez na posição: {primeira}')
print(f'A letra A aparece pela última vez na posição: {ultima}')