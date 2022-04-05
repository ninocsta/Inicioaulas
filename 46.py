'''
Exercício Python 43: Desenvolva uma lógica que leia o
peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
imc = peso / altura ** 2
'''
peso = float(input('Digite seu peso:\n'))
altura = float(input('Digite sua altura:\n'))
imc = peso / altura ** 2
print(f'Seu IMC é {imc:,.2f}')
if imc < 18.5:
    print('Vish, abaixo do peso :/')
elif imc < 25:
    print('Parabéns, você está no peso ideal.')
elif imc < 30:
    print('Cuidado, está com sobrepeso.')
elif imc < 40:
    print('Cuidado redobrado, já é consideradp obesidade.')
else:
    print('Procure um médico, obesidade mórbida.')