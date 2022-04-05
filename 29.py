'''
leia um numero de 0 a 9999 e mostre cada um separado:
unidade
dezena
centena
milhar


'''

n = int(input('Digite um número de 1 a 9999:\n'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Anallisando o número: {n}')
print(f'Unidade: {[u]}')
print(f'Dezena: {[d]}')
print(f'Centena: {[c]}')
print(f'Milhar: {[m]}')


