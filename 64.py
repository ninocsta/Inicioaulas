'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
while True
-- fazer cadastro
-- solicitar idade/sexo de cada pessoa
-- depois de cada cadastro, perguntar se quer continuar a cadastrar
i = s = mm = 0
A- if idade >= 18
i += 1

B- if sexo == homem
s += 1

C- if sexo == mulher and idade < 20 anos
mm += 1
'''

a = b = c = count = 0
print('~~' * 15)
print('Área de cadastro de pessoas')
print('~~' * 10)
while True:
    idade = int(input('Qual a idade? '))
    if idade >= 18:
        a += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? [M/F]: ')).strip().upper()[0]
        if sexo in 'Mm':
            b += 1
        if sexo in 'Ff' and idade < 20:
            c += 1
    count += 1
    print('Cadastro realizado com sucesso!.')
    continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]

    if continuar in 'Ss':
        print('Continuando...')

    else:
        break

print(f'{a} pessoas tem mais de 18 anos.')
print(f'{b} homens foram cadastrados.')
print(f'{c} mulheres com menos de 20 anos foram cadastradas.')
print(f'No total, foram realizados {count} cadastros.')

