'''Exercício Python 39: Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


input ano de nascimento
nasceu em 2004, hora de se alistar
antes de 2004, já passou a hora de se alistar, 2004 - a idade
2005 pra cima, ainda nao chegou a hora de se alistar, idade - 2004 pra ver o tempo faltante pra se alistar

'''
from datetime import date

nasc = int(input('Em que ano você nasceu ? '))
atual = date.today().year
idade = atual - nasc
if idade == 18:
    print('Parabéns, é hora de se alistar!!!')
elif idade > 18:
    a = idade - 18
    print(f'Que pena, já passou {a} anos do seu alistamento.')

elif idade < 18:
    a = 18 - idade
    print(f'Opa, parece que ainda falta(m){a} anos para você se alistar.')







'''if a == 2004:
    print('Parabéns, é hora de se alistar!!!')
elif a > 2004:
    a = a - 2004
    print(f'Opa, parece que ainda falta(m){a} anos para você se alistar.')
else:
    a = 2004 - a
    print(f'Que pena, já passou {a} anos do seu alistamento.')
'''