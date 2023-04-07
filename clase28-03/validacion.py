'''
Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.
'''

fecha = input('Ingrese una fecha dd/mm/aaaa: ')

def calcularDiaJuliano(dia,mes,año,fecha):
    feb = 0
    dias = 0
    
    if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
        feb = 29
    else:
        feb = 28

    diaMes = [31,feb,31,30,31,30,31,31,30,31,30,31]

    for i in range(mes-1):
        dias += diaMes[i]
    dias += dia
    print( fecha, ' es el dia ', dias, ' del año ', año)


def validacion(fecha):
    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    año = int(fecha[6:10])
    if mes >12 or mes <= 0:
        print('Mes incorrecto')
    elif año <= 0:
        print('Año incorrecto')
    elif mes == 1 or mes  == 3 or mes == 5 or mes  == 7 or mes  == 9 or mes == 12:
        if dia <=0 or dia > 31:
            print('Dia incorrecto')
    elif mes == 4 or mes == 6 or mes ==9 or mes == 11:
        if dia <= 0 or dia > 30:
            print('Dia incorrecto')
    elif año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
        if mes == 2:
            if dia <=0 or dia > 29:
                print('Dia incorrecto')
    elif mes == 2:
        if dia <= 0 or dia > 28:
            print('Dia incorrecto')
    else:
         return calcularDiaJuliano(dia,mes,año,fecha)


validacion(fecha)
x = validacion(fecha)

print(x)