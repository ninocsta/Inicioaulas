'''
Exercício Python 44: Elabore um programa que calcule o
valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros

valor do produto
condicao de pagamento
'''
vp = float(input('Qual o valor do produto?\n'))
fp = int(input('''Digite o número que corresponda com a forma de pagamento
1- dinheiro/cheque
2- 1x cartão
3- 2x cartão
4- 3x ou mais cartão
'''))
if fp == 1:
    vp = vp * 90 / 100
    print(f'Com essa forma de pagamento, o valor do produto sairá por apenas R${vp}')
elif fp == 2:
    vp = vp * 95 / 100
    print(f'Com essa forma de pagamento, o valor do produto sairá por apenas R${vp}')
elif fp == 3:
    print(f'Com essa forma de pagamento, o valor do produto sairá por R${vp}')
elif fp == 4:
    vp = vp * 120 / 100
    print(f'Com essa forma de pagamento, o valor do produto sairá por R${vp} sendo 20% de juros.')
else:
    print('Opção inválida, tente novamente!')
