# Elabore um programa que calcule o valor a ser pago por um produto.
# Considere o seu preço normal e condição de pagamento:
# À vista (dinheiro/cheque): 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: Preço normal;
# 3x ou mais no cartão: 20% juros.
print('\033[1;31;40m{:=^40}\033[m'.format(' LOJAS ALMEIDA '))
preco = float(input('Valor das compras: R$ '))
print('\n1 - À vista (dinheiro/cheque) \n2 - À vista (cartão)' +
'\n3 - Em até 2x no cartão \n4 - 3x ou mais no cartão')
pgto = int(input('Escolha uma condição de pagamento com base no menu acima: '))

if pgto == 1:
    total = preco - (preco * (10 / 100))
elif pgto == 2:
    total = preco - (preco * (5 / 100))
elif pgto == 3:
    total = preco
    parc = total / 2
    print(f'\nSua compra será parcelada em 2x \033[1;32msem juros\033[m de R$ {parc:.2f}', end='')
elif pgto == 4:
    total = preco + (preco * (20 / 100))
    total_parc = int(input('Quantidade de parcelas: '))
    parc = total / total_parc
    print(f'\nSua compra será parcelada em {total_parc}x de {parc:.2f}\033[31m*\033[m', end='')
else:
    total = preco
    print('\nOpção de pagamento inválida. Tente novamente!', end='')

print(f'\nTotal a pagar: R$ {total:.2f}\n')