#aumento  1250+ 10%
#1250 - 15%
s = int(input('Digite seu salário para ganhar um aumento: \n'))
if s >= 1250:
    a = s * 110 / 100
    print(f'Seu novo salário ´é de {a} e o aumento foi de {a - s}')
else:
    a2 = s * 115 / 100
    print(f'Seu novo salário é de {a2} e o aumento foi de {a2 - s}')
    