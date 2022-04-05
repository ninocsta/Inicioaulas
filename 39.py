n1 = int(input('Digite um número\n'))
n2 = int(input('Digite outro número\n'))
n3 = int(input('Digite mais um núemro\n'))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f'{maior} é o maior.')

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'{menor} é o menor')
