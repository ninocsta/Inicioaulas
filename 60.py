'''
Exercício Python 62: Melhore o DESAFIO 61,
perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.

x termos
an = a1 + (n – 1) . r

'''
p1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da sua PA? '))
count = 0
n = 1
p = 1
qt = 10

while count != qt:
    pa = p1 + (n - 1) * r
    n += 1
    count += 1

    print(f'--> {pa}', end='')
    if count == qt:
        mais = int(input(' Quantos termos quer ver a mais? '))
        qt = qt + mais
        if mais == 0:
            break
print(f'Progressão finalizada com {count} termos.')
print('FIM!')
