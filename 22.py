import math
co = float(input('Diga o cateto oposto:\n'))
ca = float(input('Diga o cateto adjacente: \n'))
h = co ** 2 + ca ** 2
print(f'A hipotenusa é {math.sqrt(h)}')

hi = math.hypot(co, ca)
print(f'{hi}')
