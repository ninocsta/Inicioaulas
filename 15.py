#descobrir quanto foi a % do aumento



#a = (vf * 100) / vi
#p = r - 100
#input valor inicial
#input valor final
#print porcentagem

vi = float(input('Digite seu salário inicial: '))
vf = float(input('Digite o salário que você ganha agora: '))
a = (vf * 100) / vi
p = a - 100
print(f'O aumento que você teve de salário, do início até agora é de {p}%')
