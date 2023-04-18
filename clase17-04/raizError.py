import math
cont = 0
sumatoria = 0
bandera = True

while bandera:
    try:
        n = int(input('Ingrese un numero '))
        raiz = math.sqrt(n)
        sumatoria += raiz
        if n == 0:
            bandera = False
        else:
            cont +=1
    except ValueError:
        print('Ingrese solo numeros enteros positivos')
    
if cont != 0:
    print('El promedio es ',sumatoria/cont)
    print('la sumatoria es ', sumatoria)
    print('Numeros ingresados ',cont)
else:
    print('No se ingresaron datos validos')