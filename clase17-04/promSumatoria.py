cont = 0
sumatoria = 0
bandera = True

while bandera:
    try :
        n = float(input('Ingrese un numero '))
        sumatoria += n
        if n == 0:
            bandera = False
        else:
            cont += 1
    except ValueError:
        print('Digite solo numeros')
    
if cont != 0:
    print('El promedio es ',sumatoria/cont)
    print('la sumatoria es ', sumatoria)
    print('Numeros ingresados ',cont)
else:
    print('No se ingresaron datos validos')
