'''
Exercício Python 70: Crie um programa que
leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não.
 No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
- cadastro de produto
input nome
input preço
preço = 0
a- preço += preço
b- if preço >= 1000
p += 1

- deseja continuar cadastrando ?
'''
print('~~' * 15)
print('Área de carrinho de produtos.')
print('~~' * 15)
p = m1 = 0
n = ' '
menor = 0
count = 0
while True:
    nome = str(input('Nome: '))
    preço = float(input('Preço: '))
    p += preço
    count += 1
    if count == 1:
        menor = preço
        n = nome
    if preço < menor:
        menor = preço
        n = nome
    if preço >= 1000:
        m1 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'S':
        print('Continuando...')
    if continuar in 'N':
        print('Fechando carrinho...')
        break

print(f'O total gasto foi de R${p:.2f}')
print(f'{m1} produtos custam mais de R$1000,00.')
print(f'O produto mais barato é {n}, que custa R${menor:.2f}.')