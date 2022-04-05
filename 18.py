#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

#input km percorridos
#input dias
#60 dia
#0,15 por km
#preço a pagar = km * 0,15 + dias*60

km = float(input('Quantos km foram percorridos? '))
d = float(input('Quantos dias o carro ficou alugado? '))
kma = km * 0.15
da = d * 60
vp = kma + da


print(f'O valor total a pagar é de {round(vp, 2)}, sabendo que foram {da} reais por {d} dias e {kma} reais por {km}km')
