'''
Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:

    Se divide el número mayor entre el menor.
    Si la división es exacta, el divisor es el MCD.
    Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.

Crea un programa principal que lea dos números enteros y muestre el MCD.
'''

def calcularMCD(num1,num2):

    if num1 > num2:
        if num1%num2 == 0:
            return num2
        else:
           return calcularMCD(num2,(num1%num2))
    elif num2 > num1:
        if num2%num1 == 0:
            return num1
        else:
           return calcularMCD(num1,(num2%num1))

x = calcularMCD(0,125)
print(x)











