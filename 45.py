'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

valor dos lados dos triangulos:
'''
l1 = int(input('Digite o lado um: \n'))
l2 = int(input('Digite o lado dois: \n'))
l3 = int(input('Digite o lado três: \n'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Pode formar triângulo')
    if l1 == l2 == l3:
        print('Triângulo EQUILÁTERO')
    elif l1 != l2 != l3:
        print('Triângulo ESCALENO.')
    else:
        print('Triângulo ISÓSCELES')
else:
    print('Não pode formar triângulo!')
