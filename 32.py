#nome inicial e final da pessoa separadamente


nc = str(input('Qual é o seu nome completo?\n')).strip()
print(f'Prazer em te conhecer {nc}')
n = nc.split()

print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n)-1]}')
