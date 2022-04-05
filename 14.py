#calcular o desconto ou aumento em %
#input %
#input valor inicial
#print valor final
# r = %/100 x valor total
# valor final = valor inicial + r

vi = float(input('Qual o seu salário inicial? '))
p = float(input('Quanto % de aumento ? '))

r = (p / 100) * vi

vf = vi + r
print(f'O seu novo salário é de R${vf}')
