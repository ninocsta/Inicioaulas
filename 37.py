#distancia de uma viagem input
#,50 por km até 200km
#,45 por km se mais de 200km
d = int(input('Qual a distância da viagem?\n'))
if d <= 200:
    dd = d * 0.50
    print(f'Sua viagem custará {dd} reais.')
else:
    ddd = d * 0.45
    print(f'Sua viagem custará {ddd} reais.')
