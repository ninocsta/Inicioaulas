a = int(input('Digite um ano para descobrir se ele é bissexto: \n'))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'{a} é ano bissexto!')
else:
    print('Não é bissexto!')