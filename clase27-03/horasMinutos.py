'''
Escribir dos funciones que permitan calcular:

    La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.
'''
h = 0
m = 0
s= 0

def calcularSegundos(h,m,s):
    h = int(input('Ingrese las horas '))
    m = int(input('Ingrese los minutos '))
    s = int(input('Ingrese las segundos '))
    s = s + m*60 + h*3600
    return s

x = calcularSegundos(h,m,s)
print(x)

def calcularHoras(m,s):
    m = float(input('Ingrese los minutos '))
    s = float(input('Ingrese los segundos '))
    h = s/3600 + m/60
    return h

x = calcularHoras(m,s)
print(round(x,2))











