'''
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
'''

def calcularTemperatura():
    temMax = float(input('Ingrese la temperatura maxima '))
    temMin = float(input('Ingrese la temperatura minima '))
    print('La temperatura media es ',(temMax+temMin)/2)
    
def mostrarMediaPorDias():
    dias = int(input('Ingrese el numero de dias '))
    for i in range(dias):
        calcularTemperatura()

mostrarMediaPorDias()











