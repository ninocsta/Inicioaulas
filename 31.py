#quantas x aparece a letra a
#quando ela começa
#quando ela termina

c = str(input('Digite uma frase \n')).lower()

a = c.count('a')
f = c.find('a')+1
fr = c.rfind('a')+1

print(f'A letra a aparece {a} vezes.')
print(f'A letra a aparece primeiro na posição {f}')
print(f'A letra a aparece por último na posição {fr}')
