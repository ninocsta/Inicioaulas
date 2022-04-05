'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


'''
count = t = ma = 0

me = 999999999999999999999

while True:
    n = int(input('Digite um número inteiro: '))

    t += n
    count += 1
    if n >= ma:
        ma = n
    if n <= me:
        me = n
    c = str(input('Deseja continuar? [S/N] ')).upper()
    if c in 'S':
        print('Continuando...')

    else:
        break


m = t / count
print(f'O valor total foi de {t}')
print(f'A média dos valores foi de: {m}')
print(f'O maior número digitado foi o {ma}')
print(f'O menor número digitado foi o {me}')
