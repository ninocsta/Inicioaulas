'''
Exercício Python 45: Crie um programa que
faça o computador jogar Jokenpô com você.

gerar random
input pedra papel ou tesoura
if random =
'''
from random import randint
itens = ('pedra', 'papel', 'tesoura')
jogador = int(input('''Escolha uma opção:
[0]pedra
[1]papel
[2]tesoura
'''))
computador = randint(0, 2)
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PÔ')
sleep(3)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('Pedra com pedra, empate!')
    elif jogador == 1:
        print('Papel ganha de tesoura, parabéns.')
    else:
        print('Pedra ganha de tesoura, não foi dessa vez.')
elif computador == 1:
    if jogador == 0:
        print('Pedra perde para papel, perdeu')
    elif jogador == 1:
        print('Papel empata com papel')
    else:
        print('Tesoura ganha de papel, boa!')
elif computador == 2:
    if jogador == 0:
        print('Pedra ganha de tesoura, boa')
    elif jogador == 1:
        print('Papel perde pra tesoura :/')
    else:
        print('Iguais empata zz')
