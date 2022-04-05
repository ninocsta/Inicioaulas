# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

v = float(input('Digite um valor, para ver seus centímetros e milímetros: '))
v1 = v * 100
v2 = v * 1000
print(f'{v}cm metros tem {v1} centímetros e {v2} milímetros')
