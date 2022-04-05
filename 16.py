#preço do produto com 5% de desconto

vp = float(input('Qual o valor do produto? '))
d = vp * 0.05
vf = vp - d
print(f'Parabéns, você ganhou um desconto de 5% {d} reais, e o valor com desconto ficou apenas {round(vf,2)} reais.')
