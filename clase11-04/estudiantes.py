for i in range(3):
    nombre = input('Ingrese el nombre del estudiante ')
    nota1 = float(input('Ingrese la nota 1 '))
    nota2 = float(input('Ingrese la nota 2 '))
    nota3 = float(input('Ingrese la nota 3 '))
    notafinal = round((nota1+nota2+nota3)/3,2)
    if notafinal >= 3.0:
        print('El estudiante', nombre, 'aprobo la materia con', notafinal)
    elif notafinal < 3.0:
        print('El estudiante', nombre, 'reprobo la materia con', notafinal)

    

