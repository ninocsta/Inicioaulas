'''
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8


'''
print('-=-Sequência de Fibonacci-=-')
qt = int(input('Quantos termos você quer ver? '))

count = 2
t1 = 0
t2 = 1
print(f'{t1} --> {t2}', end='')
t3 = t1 + t2
while count < qt:
    t3 = t1 + t2
    print(f' --> {t3}', end='')
    t1 = t2
    t2 = t3
    count += 1
