#3 retas formam um triangulo ?
r1 = int(input('Digite o valor de uma das retas\n'))
r2 = int(input('Digite o valor de uma das retas\n'))
r3 = int(input('Digite o valor de uma das retas\n'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Sim, formam um triângulo')
else:
    print('\033[1;31;43mNão é possível formar um triângulo\033[m')
