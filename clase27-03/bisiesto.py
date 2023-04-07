'''
El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

    LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
    DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
    EsBisiesto: Recibe un año y nos dice si es bisiesto.
    Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

'''


fecha = input('Ingrese una fecha dd/mm/aaaa; ')
dia = int(fecha[0:2])
mes = int(fecha[3:5])
año = int(fecha[6:10])
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
print(fecha, ' es el dia ', dias, ' del año ', año)

