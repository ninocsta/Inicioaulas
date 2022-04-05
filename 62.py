'''
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e
 qual foi a soma entre eles (desconsiderando o flag).


'''
count = 0
c = 0
t = 0
print('~~~' * 9)
print('Soma de números inteiros')
print('Digite 999 para encerrar.')
print('~~~' * 9)
while True:
    n = int(input('Digite um número inteiro '))
    if n == 999:
        print('Programa encerrado!')
        break
    p = t
    t = n + p
    count += 1


print(f'O valor  total da soma foi de {t}.')
print(f'O total de números somados foi {count}.')
