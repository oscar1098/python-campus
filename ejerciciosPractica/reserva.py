print('Ingrese la clase en la que desea volar:\n1.Primera clase con un valor de 450000\n2.Clase ejecutiva con un valor de 250000\n3.Clase turista con un valor de 150000')
x = int(input(':)_'))

if x == 1:
    print('Seleccione el periodo en el que va a hacer la reservacion: \n1.Entre 6 y 4 semanas antes del vuelo recargo del 10%\n2.Entre 4 y 2 semanas antes del vuelo recargo del 25%\n3.Entre 2 semanas y 2 dos dias antes del vuelo recargo del 45%\n4.Entre 2 dias y 0 dias antes del vuelo recargo del 60%')
    y = int(input(':)_'))
    if y == 1:
        print('El valor de su vuelo es: ','$ ',450000*1.1)
    elif y == 2:
        print('El valor de su vuelo es: ','$ ',450000*1.25)
    elif y == 3:
        print('El valor de su vuelo es: ','$ ',450000*1.45)
    elif y == 4:
        print('El valor de su vuelo es: ','$ ',450000*1.6)
if x == 2:
    print('Seleccione el periodo en el que va a hacer la reservacion: \n1.Entre 6 y 4 semanas antes del vuelo recargo del 10%\n2.Entre 4 y 2 semanas antes del vuelo recargo del 25%\n3.Entre 2 semanas y 2 dos dias antes del vuelo recargo del 45%\n4.Entre 2 dias y 0 dias antes del vuelo recargo del 60%')
    y = int(input(':)_'))
    if y == 1:
        print('El valor de su vuelo es: ','$ ',250000*1.1)
    elif y == 2:
        print('El valor de su vuelo es: ','$ ',250000*1.25)
    elif y == 3:
        print('El valor de su vuelo es: ','$ ',250000*1.45)
    elif y == 4:
        print('El valor de su vuelo es: ','$ ',250000*1.6)
if x == 3:
    print('Seleccione el periodo en el que va a hacer la reservacion: \n1.Entre 6 y 4 semanas antes del vuelo recargo del 10%\n2.Entre 4 y 2 semanas antes del vuelo recargo del 25%\n3.Entre 2 semanas y 2 dos dias antes del vuelo recargo del 45%\n4.Entre 2 dias y 0 dias antes del vuelo recargo del 60%')
    y = int(input(':)_'))
    if y == 1:
        print('El valor de su vuelo es: ','$ ',150000*1.1)
    elif y == 2:
        print('El valor de su vuelo es: ','$ ',150000*1.25)
    elif y == 3:
        print('El valor de su vuelo es: ','$ ',150000*1.45)
    elif y == 4:
        print('El valor de su vuelo es: ','$ ',150000*1.6)
