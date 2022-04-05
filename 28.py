'''
nome completo com
letras maiusculas
letras minusculas
qtas letras no total
qtas letras tem o primeiro nome
'''

n = str(input('Digite seu nome completo:\n')).strip()
e = n.count(' ')
print(f'Seu nome em letras maiúsculas: {n.upper()}')
print(f'Seu nome em letras minúsculas: {n.lower()}')
print(f'Seu nome possui no total: {len(n)}')
print(f'Seu nome sem os espaços tem {len(n) - e}')
l = n.split()
print(f'O primeiro nome tem {len(l[0])} letras')
separa = n.find(' ')
print(f'O primeiro nome é {separa}')
