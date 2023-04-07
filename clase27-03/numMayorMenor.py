'''
Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
'''

numeros = []
numMayorMenor = [0.0,0.0]

def calcularMaxMin (arreglo,arreglo2):
    numMayor = 0
    numMenor = 0
    bandera = True
    while bandera:
        x = float(input('\nIngrese un numero\n'))
        arreglo.append(x)
        x = input('\nIngresar otro numero S/N\n').upper()
        if x == 'N':
            bandera = False
    for numero in arreglo:
        if numero > numMayor:
            numMayor = numero
        if numero < numMenor:
            numMenor = numero
    arreglo2[0] = numMayor
    arreglo2[1] = numMenor
    return arreglo2

calcularMaxMin(numeros, numMayorMenor)
print('El numero mayor es: ', numMayorMenor[0])
print('El numero menor es: ', numMayorMenor[1])
print(numeros)









