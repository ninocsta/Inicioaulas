'''
Exercício Python 53: Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo, desconsiderando os
 espaços. Exemplos de palíndromos:
'''
frase = str(input('Digite um palíndromo: \n'))
letras = len(frase.replace(" ",""))
inverso = ''
for c in range(letras - 1, -1, -1):
    inverso += letras[c]
print(letras, inverso)
