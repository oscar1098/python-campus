'''
2.      Escribir un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es:  Celsius = (5/9) * (Fahrenheit-32)'''

x = float(input('Ingrese la temperatura en Fahrenheit '))
y = (5/9)*(x-32)
print(x,' Fahrenheit es equivalente a ',y, ' grados Celsius')

