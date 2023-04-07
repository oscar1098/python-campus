import math

menu = True
r = 0
l=0
b = 0
h = 0
a = 0
n = 0
moneda = ['',0.0,0.0]
solucionEcuacion = [0.0,0.0]
m = ''
z = 0
v = 0
w = 0

def calcularAreaCirculo(r):
    r = int(input('\nIngrese el valor del radio: '))
    return 3.1416*(r**2)

def calcularAreaCuadrado(l):
    l = int(input('\nIngrese el valor del lado: '))
    return l*l

def calcularAreaTriangulo(b,h):
    b = int(input('\nIngrese el valor de la base '))
    h = int(input('\nIngrese el valor de la alrtura '))
    return (b*h)/2

def concerNumeroPrimo(n):
    n = int(input('\nIngrese el numero\n'))
    primo = []
    for i in range(n):
        if n % (i+1) == 0:
            primo.append(i+1)
    if len(primo) == 2:
        return True
    else:
        return False

def calcularFactorial(f):
    f = int(input('Ingrese un numero '))
    factorial = 1

    for i in range(f):
        factorial *= (i+1)
    return factorial

def convertirMoneda(arreglo):
    arreglo[0] = input('\nIngrese la moneda a la que desea convertir (dolares, yenes o libras) ')
    arreglo[1] = int(input('\nIngrese la cantidad de pesos que desea convertir '))

    if arreglo[0] .upper() == 'DOLARES':
        arreglo[2] = arreglo[1]/4779.28
        return arreglo
    elif arreglo[0].upper() == 'YENES':
        arreglo[2] = arreglo[1]/36.33
        return arreglo
    elif arreglo[0].upper() == 'LIBRAS':
        arreglo[2] = arreglo[1]/5807.25
        return arreglo

def resolverEcuacion(a,b,c,arreglo):
    a = float(input('Ingresa el valor de a '))
    b = float(input('Ingresa el valor de b '))
    c = float(input('Ingresa el valor de c '))

    d = b**2-(4*a*c)
    if d >= 0:
        arreglo[0] = (-b+(math.sqrt(d)))/2*a
        arreglo[1] = (-b-(math.sqrt(d)))/2*a
        return arreglo
    elif d < 0:
        return '\nEs un numero imaginario'


while menu:
    x = input('\nSeleccione que desea realizar:\n1.Para hallar area de un circulo cuadrado o triangulo\n2.Indicar si un numero es primo\n3.Factorial de un numero\n4.Convertir monedas\n5.Resolver ecuacion cuadratica\n6.Para salir \n')
    if x == '1':
        calcular = True
        while calcular:
            y = input('\nSeleccione la figura:\n1.Para circulo\n2.Para cuadrado\n3.Para Triangiulo\n4.Para salir \n')
            if y == '1':
                a = calcularAreaCirculo(r)
                print('\nEl area del circulo es: ', a)
            elif y == '2':
                a = calcularAreaCuadrado(l)
                print('\nEl area del cuadrado es: ', a)
            elif y == '3':
                a = calcularAreaTriangulo(b,h)
                print('\nEl area del triangulo es: ', a)
            elif y == '4':
                calcular = False

    if x == '2':
        a = concerNumeroPrimo(n)
        print(a)
    if x == '3':
        a = calcularFactorial(5)
        print(a)
    if x == '4':
        convertirMoneda(moneda)
        print('\n',moneda[1],' pesos colombianos ', ' es igual a ',moneda[2],' ',moneda[0])
    if x == '5':
        a = resolverEcuacion(z,v,w,solucionEcuacion)
        print(a)
    if x == '6':
        menu = False