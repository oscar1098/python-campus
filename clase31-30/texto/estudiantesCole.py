import os
'''
Estudiantes         materias        notas
id                  id              id
nombre              nombre          id estudiante
apellidos                           id materia
correo                              nota1
                                    nota2
                                    nota3
                                    notaFinal
'''                                 

print('\n\n\n')
count = 0
estudiantes = {
    1: {
        'nombre': 'Oscar',
        'apellido': 'apellido1',
        'correo' : 'correo1@gmail.com'
    },
    2: {
        'nombre': 'Laura',
        'apellido': 'apellido2',
        'correo' : 'correo2@gmail.com'
    },
    3: {
        'nombre': 'Nicolas',
        'apellido': 'apellido3',
        'correo' : 'correo3@gmail.com'
    },
    4: {
        'nombre': 'Andres',
        'apellido': 'apellido4',
        'correo' : 'correo4@gmail.com'
    },
    5: {
        'nombre': 'Angie',
        'apellido': 'apellido5',
        'correo' : 'correo5@gmail.com'
    },
}

dicMaterias = {
    1 : {
        'nombre':'matematicas'
    },
    2 : {
        'nombre': 'Fisica'
    },
    3 : {
        'nombre': 'Lenguaje'
    },
    4 : {
        'nombre': 'Quimica'
    },
    5 : {
        'nombre': 'Ingles'
    }
}

dicNotas = {
    1:{
    'idEstudiante' : '',
    'idMateria' : '',
    'nota1' : '',
    'nota2' : '',
    'nota3' : '',
    'notaFinal' : ''
}

}
# OPCION

def verMenu():
    os.system('clear')
    print('***********************COLE***********************')
    print('''Seleccione alguna de las siguientes opciones
    1.Notas     2.Estudiantes
    3.Materias  0.Salir
    ''')

# MATERIAS

def verMaterias(materias):
    os.system('clear')
    print('***********************MATERIAS***********************')
    print('CODIGO\t\tNOMBRE\n')
    for materia in materias:
        print(materia, '\t\t\t',materias[materia]['nombre'])
    print('''Seleccione alguna de las siguientes opciones
    1.Agregar    2.Editar
    3.Eliminar  0.Salir
    ''')

# ESTUDIANTES
def verEstudiantes(estudiantes):
    os.system('clear')
    print('***********************ESTUDIANTES***********************')
    print('CODIGO\t\t\tNOMBRE\t\t\t\tAPELLIDO\t\t\tCORREO')
    for estudiante in estudiantes:
        print(estudiante, '\t\t\t',estudiantes[estudiante]['nombre'],'\t\t\t',estudiantes[estudiante]['apellido'],'\t\t\t',estudiantes[estudiante]['correo'])
    print('''Seleccione alguna de las siguientes opciones
    1.Agregar    2.Editar
    3.Eliminar  0.Salir
    ''')
# VER NOTAS
def verNotas(notas):
    os.system('clear')
    print('***********************ESTUDIANTES***********************')
    print('CODIGO\t\tCODIGO ESTUDIANTE\t\tCODIGO MATERIA\t\tNOTA1\t\t\tNOTA2\t\t\tNOTA3\t\t\tNOTA FINAL')
    for nota in notas:
        print(nota,'\t\t',notas[nota]['idEstudiante'],'\t\t\t',notas[nota]['idMateria'],'\t\t',notas[nota]['nota1'],'\t\t\t',notas[nota]['nota2'],'\t\t\t',notas[nota]['nota3'],'\t\t\t',notas[nota]['notaFinal'])
    print('''\nSeleccione alguna de las siguientes opciones
    1.Agregar    2.Editar
    3.Eliminar  0.Salir
    ''')
    
verMenu()
opcMenu = input()

while opcMenu != '0':
    if opcMenu == '1':
        print('***********************NOTAS***********************')
        verNotas(dicNotas)
        opc1 = input()
        if opc1 == '1':
            os.system('clear')
            print('***********************AGREGAR***********************')
            if count == 0:
                id = list(dicNotas.keys())[-1]+1
                for materias in dicMaterias:
                    for estudiante in estudiantes:    
                        dicNotas[id]={
                            'idEstudiante' : estudiantes[estudiante]['nombre'],
                            'idMateria' : dicMaterias[materias]['nombre'],
                            'nota1' : 'p',
                            'nota2' : 'p',
                            'nota3' : 'p',
                            'notaFinal' : 'p'
                        }
                        id += 1
                        count = 1
            for materia in dicMaterias:
                print(materia, '\t\t\t',dicMaterias[materia]['nombre'])
            idMateria = int(input('\nIngrese el id de la materia'))
            for key in list(dicNotas.keys()):
                if dicNotas[key]['nota1'] != 'p' and dicNotas[key]['nota2'] != 'p' and dicNotas[key]['nota3'] != 'p':
                    print('\nYa se ingresaron notas ')
                elif dicNotas[key]['idMateria'] == dicMaterias[idMateria]['nombre'] and dicNotas[key]['nota2'] != 'p':
                    print('Ingrese la nota 3 del estudiante ', dicNotas[key]['idEstudiante'],' en la materia ', dicNotas[key]['idMateria'],' ' )
                    nota3 = float(input())
                    dicNotas[key]['nota3'] = nota3
                    dicNotas[key]['notaFinal'] = (nota1+nota2+nota3)/3
                elif dicNotas[key]['idMateria'] == dicMaterias[idMateria]['nombre'] and dicNotas[key]['nota1'] != 'p':
                    print('Ingrese la nota 2 del estudiante ', dicNotas[key]['idEstudiante'],' en la materia ', dicNotas[key]['idMateria'],' ' )
                    nota2 = float(input())
                    dicNotas[key]['nota2'] = nota2
                elif dicNotas[key]['idMateria'] == dicMaterias[idMateria]['nombre'] and dicNotas[key]['nota1'] == 'p':
                    print('Ingrese la nota 1 del estudiante ', dicNotas[key]['idEstudiante'],' en la materia ', dicNotas[key]['idMateria'],' ' )
                    nota1 = float(input())
                    dicNotas[key]['nota1'] = nota1
                
        
        elif opc1 == '2':
            os.system('clear')
            print('***********************EDITAR***********************')
            verNotas(dicNotas)
            idNota = int(input('Ingrese el id de la nota '))
            opcNotas = input(('Ingrese \n1.Editar Estudiante\n2.Editar materia\n3.Editar nota 1\n4.Editar nota 2\n5.Editar nota 3\n6.Editar nota final\n7.Editar todo\n0.Para salir\n'))
            while opcNotas != '0':
                if opcNotas == '1':
                    os.system('clear')
                    for estudiante in estudiantes:
                        print(estudiante, '\t\t\t',estudiantes[estudiante]['nombre'],'\t\t\t',estudiantes[estudiante]['apellido'])
                    idEstudiante = int(input(('\nIngrese el id del destudiante ')))
                    dicNotas[idNota]['idEstudiante'] = estudiantes[idEstudiante]['nombre']
                elif opcNotas == '2':
                    os.system('clear')
                    for materia in dicMaterias:
                        print(materia, '\t\t\t',dicMaterias[materia]['nombre'])
                    idMateria = int(input(('\nIngrese el id de la materia ')))
                    dicNotas[idNota]['idMateria'] = dicMaterias[idMateria]['nombre']
                elif opcNotas == '3':
                    os.system('clear')
                    print(idNota,'\t\t',dicNotas[idNota]['idEstudiante'],'\t\t',dicNotas[idNota]['idMateria'],'\t\t',dicNotas[idNota]['nota1'],'\t\t',dicNotas[idNota]['nota2'],'\t\t',dicNotas[idNota]['nota3'],'\t\t\t',dicNotas[idNota]['notaFinal'])
                    nota1 = int(input(('\nIngrese la nota 1 ')))
                    dicNotas[idNota]['nota1'] = nota1
                elif opcNotas == '4':
                    os.system('clear')
                    print(idNota,'\t\t',dicNotas[idNota]['idEstudiante'],'\t\t',dicNotas[idNota]['idMateria'],'\t\t',dicNotas[idNota]['nota1'],'\t\t',dicNotas[idNota]['nota2'],'\t\t',dicNotas[idNota]['nota3'],'\t\t\t',dicNotas[idNota]['notaFinal'])
                    nota2 = int(input(('\nIngrese la nota 2 ')))
                    dicNotas[idNota]['nota2'] = nota2
                elif opcNotas == '5':
                    os.system('clear')
                    print(idNota,'\t\t',dicNotas[idNota]['idEstudiante'],'\t\t',dicNotas[idNota]['idMateria'],'\t\t',dicNotas[idNota]['nota1'],'\t\t',dicNotas[idNota]['nota2'],'\t\t',dicNotas[idNota]['nota3'],'\t\t\t',dicNotas[idNota]['notaFinal'])
                    nota3 = int(input(('\nIngrese la nota 3 ')))
                    dicNotas[idNota]['nota3'] = nota3
                elif opcNotas == '6':
                    os.system('clear')
                    print(idNota,'\t\t',dicNotas[idNota]['idEstudiante'],'\t\t',dicNotas[idNota]['idMateria'],'\t\t',dicNotas[idNota]['nota1'],'\t\t',dicNotas[idNota]['nota2'],'\t\t',dicNotas[idNota]['nota3'],'\t\t\t',dicNotas[idNota]['notaFinal'])
                    notaFinal = int(input(('\nIngrese la notaFinal ')))
                    dicNotas[idNota]['notaFinal'] = notaFinal
                elif opcNotas == '7':
                    os.system('clear')
                    for estudiante in estudiantes:
                        print(estudiante, '\t\t\t',estudiantes[estudiante]['nombre'],'\t\t\t',estudiantes[estudiante]['apellido'])
                    idEstudiante = int(input(('\nIngrese el id del destudiante ')))
                    dicNotas[idNota]['idEstudiante'] = estudiantes[idEstudiante]['nombre']
                    os.system('clear')
                    for materia in dicMaterias:
                        print(materia, '\t\t\t',dicMaterias[materia]['nombre'])
                    idMateria = int(input(('\nIngrese el id de la materia ')))
                    dicNotas[idNota]['idMateria'] = dicMaterias[idMateria]['nombre']
                    os.system('clear')
                    print(idNota,'\t\t',dicNotas[idNota]['idEstudiante'],'\t\t',dicNotas[idNota]['idMateria'],'\t\t',dicNotas[idNota]['nota1'],'\t\t',dicNotas[idNota]['nota2'],'\t\t',dicNotas[idNota]['nota3'],'\t\t\t',dicNotas[idNota]['notaFinal'])
                    nota1 = int(input(('\nIngrese la nota 1 ')))
                    dicNotas[idNota]['nota1'] = nota1
                    os.system('clear')
                    print(idNota,'\t\t',dicNotas[idNota]['idEstudiante'],'\t\t',dicNotas[idNota]['idMateria'],'\t\t',dicNotas[idNota]['nota1'],'\t\t',dicNotas[idNota]['nota2'],'\t\t',dicNotas[idNota]['nota3'],'\t\t\t',dicNotas[idNota]['notaFinal'])
                    nota2 = int(input(('\nIngrese la nota 2 ')))
                    dicNotas[idNota]['nota2'] = nota2
                    os.system('clear')
                    print(idNota,'\t\t',dicNotas[idNota]['idEstudiante'],'\t\t',dicNotas[idNota]['idMateria'],'\t\t',dicNotas[idNota]['nota1'],'\t\t',dicNotas[idNota]['nota2'],'\t\t',dicNotas[idNota]['nota3'],'\t\t\t',dicNotas[idNota]['notaFinal'])
                    nota3 = int(input(('\nIngrese la nota 3 ')))
                    dicNotas[idNota]['nota3'] = nota3
                    os.system('clear')
                    print(idNota,'\t\t',dicNotas[idNota]['idEstudiante'],'\t\t',dicNotas[idNota]['idMateria'],'\t\t',dicNotas[idNota]['nota1'],'\t\t',dicNotas[idNota]['nota2'],'\t\t',dicNotas[idNota]['nota3'],'\t\t\t',dicNotas[idNota]['notaFinal'])
                    notaFinal = int(input(('\nIngrese la notaFinal ')))
                    dicNotas[idNota]['notaFinal'] = notaFinal
                else:
                    print('opcion invalida')
                verNotas(dicNotas)
                opcNotas = input(('Ingrese \n1.Editar Estudiante\n2.Editar materia\n3.Editar nota 1\n4.Editar nota 2\n5.Editar nota 3\n6.Editar nota final\n7.Editar todo\n0.Para salir\n'))
            
        elif opc1 == '3':
            print('***********************ELIMINAR***********************')
            verNotas(dicNotas)
            id = int(input('\nIngrese el id de la nota que desea eliminar'))
            del(dicNotas[id])
            verNotas(dicNotas)
        else:
            print('opcion incorrecta')
        opcNotas = input()
    elif opcMenu == '2':
        print('***********************ESTUDIANTES***********************')
        verEstudiantes(estudiantes)
        opc = input()
        while opc != '0':
            if opc == '1':
                print('***********************CREAR***********************')
                id = list(estudiantes.keys())[len(estudiantes)-1]+1
                print('Por favor ingresa el nombre del nuevo estudiante ')
                nombre = input()
                print('Por favor ingresa el apellido del nuevo estudiante ')
                apellido = input()
                print('Por favor ingresa el correo del nuevo estudiante ')
                correo = input()
                estudiantes[id] = {
                    'nombre': nombre,
                    'apellido': apellido,
                    'correo': correo 
                    }
            elif opc == '2':
                print('***********************EDITAR***********************')
                id = int(input('Ingrese el id'))
                opc2 = input('1.Cambiar nombre\n2.Cambiar apellido\n3.Cambiar correo\n0.Salir')
                while opc2 != '0':
                    if opc2 == '1':
                        nombre = input('Ingrese el nombre ')
                        estudiantes[id]['nombre'] = nombre
                    elif opc2 == '2':
                        apellido = input('Ingrese el apellido ')
                        estudiantes[id]['apellido'] = apellido
                    elif opc2 == '3':
                        correo = input('Ingrese el correo ')
                        estudiantes[id]['correo'] = correo
                    opc2 = input('1.Cambiar nombre\n2.Cambiar apellido\n3.Cambiar correo\n0.Salir')
            elif opc == '3':
                print('***********************ELIMINAR***********************')
                id = int(input('Ingrese el id del estudiante que desea eliminar'))
                del(estudiantes[id])
            else:
                print('opcion invalida')
            verEstudiantes(estudiantes)
            opc = input()        
    elif opcMenu == '3':
        print('***********************MATERIAS***********************')
        verMaterias(dicMaterias)
        opc = input()
        while opc !='0':
            if opc == '1':
                print('***********************CREAR***********************')
                id = list(dicMaterias.keys())[len(dicMaterias)-1] + 1
                print('Por favor ingrese el nombre de la nueva materia')
                nombre = input()
                dicMaterias[id] = {'nombre': nombre}
            elif opc == '2':
                print('***********************EDITAR***********************')
                print('Por favor ingrese el codigo de la materia para editar')
                id = int(input())
                print('Por favor ingrese el nuevo nombre de la materia')
                dicMaterias[id]['nombre'] = input()
            elif opc == '3':
                print('***********************ELIMINAR***********************')
                print('Ingrese el codigo de la materia')
                id = int(input())
                del(dicMaterias[id])
            else:
                print('Por favor, seleccione una opcion valida')
            verMaterias(dicMaterias)
            opc = input()
    else:
        print('Seleccione una opcion valida')
    verMenu()
    opcMenu = input()

print('\n\n\n')









