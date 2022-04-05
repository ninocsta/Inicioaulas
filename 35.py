#+ de 80km/h recebe multa de 7,00 por km acima
v = int(input('Digite sua velocidade: \n'))
if v <= 80:
    print('Tudo certo, não levou multa')
else:
    vm = (v - 80) * 7
    print(f'Você levou multa, estava a {v}Km/h \n Sua multa é de {vm} reais.')
