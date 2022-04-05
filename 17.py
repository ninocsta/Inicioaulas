#converter celsius em farenheit
# f = celsius * 1.8 + 32

c = float(input('Informe a temperatura em °C: '))
f = c * 1.8 + 32
print(f'A temperatura de {round(c, 2)}°C é equivalente a {round(f, 2)}°F.')
