'''
Exercício Python 48: Faça um programa que calcule a
 soma entre todos os números ímpares que são múltiplos de três
 e que se encontram no intervalo de 1 até 500.
'''
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        c += n
        print(n)
print(c)
