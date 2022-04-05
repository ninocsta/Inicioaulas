'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''
num = float(input('Digite a nota da primeira prova:\n'))
ndois = float(input('Digite a nota da segunda prova: \n'))
media = (num + ndois) / 2
print(f'Sua média foi de {media} pontos.')
if media >= 7:
    print('Parabéns, você é um ótimo aluno, aprovado!!!!!!!!!!')
elif media >= 5:
    print('Que pena, ficou de recuperação.')
else:
    print('Não foi dessa vez, tente novamente ano que vem :/')
