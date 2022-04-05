import random
a = random.randint(0, 5)
n = int(input('Digite um número entre 0 e 5 \n'))
if n == a:
    print('Parabéns, você ganhou!')
else:
    print('Que pena, perdeu')
