'''
laço x no intervalo(1,10)
'''

'''
Exercício Python 54: Crie um programa que leia o ano 
de nascimento de sete pessoas. No final, mostre quantas 
pessoas ainda não atingiram a maioridade e quantas já são 
maiores.

from time import date

input 1,2,3,4,5,6,7 tem que ser inteiro, é idade.
pegar a idade, ler a idade
transformar em () sem certeza,

'''

import datetime
date = datetime.date.today().year
count = 0
for x in range(1, 8):
    nasc = int(input(f'Digite a {x} data de nascimento:\n'))
    m = date - nasc
    if m >= 21:
        count += 1
print(count)