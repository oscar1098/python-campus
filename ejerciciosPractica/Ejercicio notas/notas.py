import json
import os

cont = 0
id = 1
arregloEliminar = []
dicEstudiante = {
    '1':{
    'nombre': 'Oscar',
    'apellido': 'Ardila',
    'correo' : 'oscar@gmail.com'
    },
    '2':{
    'nombre': 'Saray',
    'apellido': 'Ortega',
    'correo' : 'saray@gmail.com'
    },
    '3':{
    'nombre': 'Laura',
    'apellido': 'Romero',
    'correo' : 'laura@gmail.com'
    },
    '4':{
    'nombre': 'Diego',
    'apellido': 'Acosta',
    'correo' : 'diego@gmail.com'
    },
    '5':{
    'nombre': 'Diana',
    'apellido': 'Fuentes',
    'correo' : 'diana@gmail.com'
    }
}

dicMaterias ={
    '1' : { 'nombre': 'Matematicas'},
    '2' : { 'nombre': 'Fisica'},
    '3' : { 'nombre': 'Quimica'}
}

dicNotas = {}
for materia in dicMaterias:
        for estudiante in dicEstudiante:
            dicNotas[str(id)] = {
                'idEstudiante':estudiante,
                'idMateria': materia,
                'nota1': 'p',
                'nota2': 'p',
                'nota3': 'p',
                'notaFinal': 'p'
            }
            id +=1

try:
    with open('./json/dicEstudiantes.json','r') as archivo:
        pruebaEs = json.load(archivo)
    archivo.close()
except FileNotFoundError:
    with open('./json/dicEstudiantes.json','w') as archivo:
        json.dump(dicEstudiante,archivo)
    archivo.close()

try:
    with open('./json/dicMaterias.json','r') as archivo:
        pruebaMa = json.load(archivo)
    archivo.close()
except FileNotFoundError:
    with open('./json/dicMaterias.json','w') as archivo:
        json.dump(dicMaterias,archivo)
    archivo.close()

try:
    with open('./json/dicNotas.json','r') as archivo:
        pruebaNota = json.load(archivo)
    archivo.close()
except FileNotFoundError:
    with open('./json/dicNotas.json','w') as archivo:
        json.dump(dicNotas,archivo)
    archivo.close()


def verMenu():
    os.system('clear')
    print('*********************MENU*********************')
    print('Seleccione:\n1.Notas\n2.Estudiantes\n3.Materias\n0.Salir')

def verMenuMaterias():
    os.system('clear')
    print('*********************MATERIAS*********************')
    print('Seleccione:\n1.Ver materias\n2.Agregar\n3.Editar\n4.Eliminar\n0.Salir')

def generarID(diccionario):
    id = str(int(list(diccionario.keys())[-1] )+ 1)
    return id

def verMaterias():
    with open('./json/dicMaterias.json','r') as archivo:
        verMaterias = json.load(archivo)
    archivo.close()
    print('CODIG0\t\t MATERIA')
    for materia in verMaterias:
        print(materia,'\t\t',verMaterias[materia]['nombre'])

def verMenuEstudiantes():
    os.system('clear')
    print('*********************ESTUDIANTES*********************')
    print('Seleccione:\n1.Ver estudiantes\n2.Agregar\n3.Editar\n4.Eliminar\n0.Salir')

def verEstudiantes():
    with open('./json/dicEstudiantes.json','r') as archivo:
        verEstudiantes = json.load(archivo)
    archivo.close()
    print('CODIGO\t\t NOMBRE\t\t APELLIDO\t\t CORREO')
    for estudiante in verEstudiantes:
        print(estudiante,'\t\t',verEstudiantes[estudiante]['nombre'],'\t\t',verEstudiantes[estudiante]['apellido'],'\t\t',verEstudiantes[estudiante]['correo'])

def menuEditarEstudiante():
    os.system('clear')
    print('*********************EDITAR ESTUDIANTES*********************')
    print('Seleccione\n1.Editar nombre\n2.Editar apellido\n3.Editar correo\n0.Salir')

def editarEstudiantes(itemCambio):
    os.system('clear')
    verEstudiantes()
    id = input('Ingrese el id del estudiante ')
    print('Ingrese el nuevo',itemCambio)
    nuevoValor = input()
    with open('./json/dicEstudiantes.json','r') as archivo:
        agregarEstudiantes = json.load(archivo)
    archivo.close()
    with open('./json/dicEstudiantes.json','w') as archivo:
        agregarEstudiantes[id][itemCambio] = nuevoValor
        json.dump(agregarEstudiantes,archivo)
    archivo.close()
    input()

def menuNotas():
    os.system('clear')
    print('*********************NOTAS*********************')
    print('Seleccione\n1.Ver notas\n2.Agregar notas\n3.Editar notas\n4.Eliminar nota\n5.Salir')

def verNotaMateria():
    os.system('clear')
    verMaterias()
    id = input('Ingrese el codigo de la materia ')
    os.system('clear')
    with open('./json/dicMaterias.json','r') as archivo:
        verMate = json.load(archivo)
    archivo.close()
    with open('./json/dicEstudiantes.json','r') as archivo:
        verEstu = json.load(archivo)
    archivo.close()
    with open('./json/dicNotas.json','r') as archivo:
        verNotas = json.load(archivo)
    archivo.close()

    print('Notas de los estudiantes en la materia',verMate[id]['nombre'])
    print('CODIGO\t\t NOMBRE\t\t NOTA 1\t\t NOTA 2\t\t NOTA 3\t\t NOTA FINAL\t\t')
    for nota in verNotas:
        if verNotas[nota]['idMateria'] == id:
            idEs = verNotas[nota]['idEstudiante']
            print(nota,'\t\t',verEstu[idEs]['nombre'],'\t\t',verNotas[nota]['nota1'],'\t\t',verNotas[nota]['nota2'],'\t\t',verNotas[nota]['nota3'],'\t\t',verNotas[nota]['notaFinal'])

def verNotaEstu():
    os.system('clear')
    verEstudiantes()
    id = input('Ingrese el codigo del estudiante ')
    os.system('clear')
    with open('./json/dicMaterias.json','r') as archivo:
        verMate = json.load(archivo)
    archivo.close()
    with open('./json/dicEstudiantes.json','r') as archivo:
        verEstu = json.load(archivo)
    archivo.close()
    with open('./json/dicNotas.json','r') as archivo:
        verNotas = json.load(archivo)
    archivo.close()

    print('Notas de las materias del estudiante',verEstu[id]['nombre'])
    print('CODIGO\t\t MATERIA\t\t NOTA 1\t\t NOTA 2\t\t NOTA 3\t\t NOTA FINAL\t\t')
    for nota in verNotas:
        if verNotas[nota]['idEstudiante'] == id:
            idMa = verNotas[nota]['idMateria']
            print(nota,'\t\t',verMate[idMa]['nombre'],'\t\t',verNotas[nota]['nota1'],'\t\t',verNotas[nota]['nota2'],'\t\t',verNotas[nota]['nota3'],'\t\t',verNotas[nota]['notaFinal'])

def editarNotas(id,leerNotas,nota):
    n = float(input('Ingrese la nota '))
    with open('./json/dicNotas.json','w') as archivo:
        leerNotas[id][nota] = n
        json.dump(leerNotas,archivo)
    archivo.close()

verMenu()
menu = input()

while menu != '0':
    if menu == '1':
        menuNotas()
        menuNota = input()
        if menuNota == '1':
            os.system('clear')
            print('*********************VER NOTAS*********************')
            print('Seleccione\n1.Ver notas por materia\n2.Ver nota por estudiante')
            menuVerNotas = input()
            if menuVerNotas == '1':
                verNotaMateria()
                input()
            elif menuVerNotas == '2':
                verNotaEstu()
                input()
            else:
                print('Seleccion invalida')

        elif menuNota == '2':
            os.system('clear')
            print('*********************AGREGAR NOTAS*********************')
            verMaterias()
            id = input('Seleccione la materia ')
            with open('./json/dicNotas.json','r') as archivo:
                leerNotas = json.load(archivo)
            archivo.close()
            with open('./json/dicMaterias.json','r') as archivo:
                leerMaterias = json.load(archivo)
            archivo.close()
            with open('./json/dicEstudiantes.json','r') as archivo:
                leerEstudiantes = json.load(archivo)
            archivo.close()
            with open('./json/dicNotas.json','w') as archivo:
                for nota in leerNotas:
                    if leerNotas[nota]['idMateria'] == id:
                        if leerNotas[nota]['nota3'] != 'p':
                            idEs = leerNotas[nota]['idEstudiante']
                            print('Calculando la nota final del estudiante',leerEstudiantes[idEs]['nombre'],'en la materia',leerMaterias[id]['nombre'])
                            nota3 = leerNotas[nota]['nota3']
                            nota2 = leerNotas[nota]['nota2']
                            nota1 = leerNotas[nota]['nota1']
                            notaFinal = nota1*0.3 + nota2*0.3 + nota3*0.4
                            leerNotas[nota]['notaFinal'] = round(notaFinal,2)
                            input()
                        elif leerNotas[nota]['nota2'] != 'p':
                            idEs = leerNotas[nota]['idEstudiante']
                            print('Ingrese la nota 3 del estudiante',leerEstudiantes[idEs]['nombre'],'en la materia',leerMaterias[id]['nombre'])
                            nota3 = float(input())
                            leerNotas[nota]['nota3'] = nota3
                        elif leerNotas[nota]['nota1'] != 'p':
                            idEs = leerNotas[nota]['idEstudiante']
                            print('Ingrese la nota 2 del estudiante',leerEstudiantes[idEs]['nombre'],'en la materia',leerMaterias[id]['nombre'])
                            nota2 = float(input())
                            leerNotas[nota]['nota2'] = nota2
                        elif leerNotas[nota]['nota1'] == 'p':
                            idEs = leerNotas[nota]['idEstudiante']
                            print('Ingrese la nota 1 del estudiante',leerEstudiantes[idEs]['nombre'],'en la materia',leerMaterias[id]['nombre'])
                            nota1 = float(input())
                            leerNotas[nota]['nota1'] = nota1
                json.dump(leerNotas,archivo)                
            archivo.close()
            input()
        elif menuNota == '3':
            os.system('clear')
            print('*********************EDITAR NOTAS*********************')
            verNotaMateria()
            id = input('\nSeleccione el estudiante del que desea editar las notas ')
            with open('./json/dicNotas.json','r') as archivo:
                leerNotas = json.load(archivo)
            archivo.close()
            if leerNotas[id]['notaFinal'] =='p':
                print('\nseleccione\n1.Editar nota 1\n2.Editar nota 2\n3.Editar nota 3')
                editarNota = input()
                if editarNota == '1' and leerNotas[id]['nota1'] != 'p':
                    editarNotas(id,leerNotas,'nota1')
                elif editarNota == '2' and leerNotas[id]['nota2'] != 'p':
                    editarNotas(id,leerNotas,'nota2')
                elif editarNota == '3' and leerNotas[id]['nota3'] != 'p':
                    editarNotas(id,leerNotas,'nota3')
                else:
                    print('No se puede editar la nota no hay registro de la nota')
            else:
                print('No se pueden editar las notas ya esta registrada la nota finalss')
            input()
        elif menuNota == '4':
            os.system('clear')
            print('*********************ELIMINAR NOTAS*********************')
            print('Seleccione\n1.Eliminar registro de notas\n2.Salir')
            op = input()
            if op == '1':
                with open('./json/dicNotas.json','r') as archivo:
                    leerNotas = json.load(archivo)
                archivo.close()
                with open('./json/dicNotas.json','w') as archivo:
                    for nota in leerNotas:
                        leerNotas[nota]['nota1'] = 'p'
                        leerNotas[nota]['nota2'] = 'p'
                        leerNotas[nota]['nota3'] = 'p'
                        leerNotas[nota]['notaFinal'] = 'p'
                    json.dump(leerNotas,archivo)
                archivo.close()
        else:
            print('Seleccion invalida')
    elif menu == '2':
        verMenuEstudiantes()
        menuEstudiantes = input()

        while menuEstudiantes != '0':
            
            if menuEstudiantes == '1':
                os.system('clear')
                print('*********************VER ESTUDIANTES*********************')
                verEstudiantes()
                input()

            elif menuEstudiantes == '2':
                os.system('clear')
                print('*********************AGREGAR ESTUDIANTES*********************')
                nombre = input('Ingrese el nombre ')
                apellido = input('Ingrese el apellido ')
                correo = input('Ingrese el correo ')
                with open('./json/dicEstudiantes.json','r') as archivo:
                    agregarEstudiantes = json.load(archivo)
                archivo.close()
                id = generarID(agregarEstudiantes)
                with open('./json/dicEstudiantes.json','w') as archivo:
                    agregarEstudiantes[id]={'nombre': nombre, 'apellido': apellido, 'correo': correo}   
                    json.dump(agregarEstudiantes,archivo)
                archivo.close()

                with open('./json/dicEstudiantes.json','r') as archivo:
                    leerEstudiantes = json.load(archivo)
                archivo.close()
                with open('./json/dicMaterias.json','r') as archivo:
                    leerMaterias = json.load(archivo)
                archivo.close()
                with open('./json/dicNotas.json','r') as archivo:
                    leerNotas = json.load(archivo)
                archivo.close()
                idN = int(generarID(leerNotas))
                with open('./json/dicNotas.json','w') as archivo:
                    for materia in leerMaterias:
                        cont = 0
                        for nota in leerNotas:
                            if leerNotas[nota]['idMateria'] == materia and leerNotas[nota]['nota1'] == 'p' and cont == 0: 
                                arregloEliminar.append(leerNotas[nota]['idMateria'])
                                cont +=1
                    for materia in arregloEliminar:
                        leerNotas[str(idN)]={
                            'idEstudiante':id,
                            'idMateria': materia,
                            'nota1': 'p',
                            'nota2': 'p',
                            'nota3': 'p',
                            'notaFinal': 'p'
                        }
                        idN += 1
                    arregloEliminar.clear()
                    json.dump(leerNotas,archivo)
                archivo.close()

            elif menuEstudiantes == '3':
                menuEditarEstudiante()
                editarEstudiante = input()

                while editarEstudiante != '0':
                    if editarEstudiante == '1':
                        editarEstudiantes('nombre')
                    elif editarEstudiante == '2':
                        editarEstudiantes('apellido')
                    elif editarEstudiante == '3':
                        editarEstudiantes('correo')
                    else:
                        print('Seleccion invalida')
                    menuEditarEstudiante()
                    editarEstudiante = input()

            elif menuEstudiantes == '4':
                os.system('clear')
                print('*********************ELIMINAR ESTUDIANTES*********************')
                verEstudiantes()
                id = input('Ingrese el id del estudiante ')

                with open('./json/dicEstudiantes.json','r') as archivo:
                    eliminarEstudiante = json.load(archivo)
                archivo.close()
                with open('./json/dicEstudiantes.json', 'w') as archivo:
                    del(eliminarEstudiante[id])
                    json.dump(eliminarEstudiante,archivo)
                archivo.close()
                with open('./json/dicNotas.json','r') as archivo:
                    eliminarEstudianteNotas = json.load(archivo)
                archivo.close()
                for estudiante in eliminarEstudianteNotas:
                    if eliminarEstudianteNotas[estudiante]['idEstudiante'] == id:
                        arregloEliminar.append(estudiante)
                with open('./json/dicNotas.json', 'w') as archivo:
                    for registro in arregloEliminar:
                        del(eliminarEstudianteNotas[registro])
                    json.dump(eliminarEstudianteNotas,archivo)
                archivo.close()
                arregloEliminar.clear()
                input('Eliminacion exitosa')
            else:
                print('Seleccion invalida')
            verMenuEstudiantes()
            menuEstudiantes = input()

    elif menu =='3':
        verMenuMaterias()
        menuMaterias = input()

        while menuMaterias != '0':

            if menuMaterias == '1':
                os.system('clear')
                print('*********************VER MATERIA*********************')
                verMaterias()
                input()

            elif menuMaterias == '2':
                os.system('clear')
                print('*********************AGREGAR MATERIA*********************')

                nombre = input('\nIngrese el nombre de la materia ')

                with open('./json/dicMaterias.json','r') as archivo:
                    agregarMaterias = json.load(archivo)
                archivo.close()
                with open('./json/dicMaterias.json','w') as archivo:
                    id = generarID(agregarMaterias)
                    agregarMaterias[id] = {'nombre' : nombre}
                    json.dump(agregarMaterias,archivo)
                archivo.close()
                with open('./json/dicEstudiantes.json','r') as archivo:
                    leerEstudiantes = json.load(archivo)
                archivo.close()
                with open('./json/dicMaterias.json','r') as archivo:
                    leerMaterias = json.load(archivo)
                archivo.close()
                with open('./json/dicNotas.json','r') as archivo:
                    leerNotas = json.load(archivo)
                archivo.close()
                id = int(generarID(leerNotas))
                idM = int(generarID(leerMaterias)) -1
                with open('./json/dicNotas.json','w') as archivo:
                    for estudiante in leerEstudiantes:
                        leerNotas[str(id)] = {
                            'idEstudiante':estudiante,
                            'idMateria': str(idM),
                            'nota1': 'p',
                            'nota2': 'p',
                            'nota3': 'p',
                            'notaFinal': 'p'
                        }
                        id += 1
                    json.dump(leerNotas,archivo)
                archivo.close()
                input()


            elif menuMaterias == '3':
                os.system('clear')
                print('*********************EDITAR MATERIA*********************')
                verMaterias()

                id = input('Ingrese el id de la materia que desea editar ')
                nombre = input('\nIngrese el nombre de la materia ')

                with open('./json/dicMaterias.json','r') as archivo:
                    editarMaterias = json.load(archivo)
                archivo.close()
                with open('./json/dicMaterias.json','w') as archivo:
                    for materia in editarMaterias:
                        if materia == id:
                            editarMaterias[materia]['nombre'] = nombre
                    json.dump(editarMaterias,archivo)
                archivo.close()
                input()

            elif menuMaterias == '4':
                os.system('clear')
                print('*********************ELIMINAR MATERIA*********************')
                verMaterias()

                id = input('Ingrese el id de la materia que desea eliminar ')

                with open('./json/dicNotas.json','r') as archivo:
                    notas = json.load(archivo)
                archivo.close()

                for nota in notas:
                    if notas[nota]['idMateria'] == id and notas[nota]['nota1'] != 'p':
                        cont += 1  

                if cont == 0:
                    with open('./json/dicMaterias.json','r') as archivo:
                        eliminarMaterias = json.load(archivo)
                    archivo.close()
                    for nota in notas:
                        if notas[nota]['idMateria'] == id :
                            arregloEliminar.append(nota)
                    with open('./json/dicNotas.json','w') as archivo:
                        for materia in arregloEliminar:
                            del(notas[materia])
                        json.dump(notas,archivo)
                    archivo.close()
                        
                    with open('./json/dicMaterias.json','w') as archivo:
                        del(eliminarMaterias[id])
                        json.dump(eliminarMaterias,archivo)
                    archivo.close()
                    arregloEliminar.clear()
                    input('Eliminacion exitosa')
                else:
                    input('Esta materia no se puede eliminar, ya tiene notas registradas')
            else:
                print('Seleccion invalida')
            verMenuMaterias() 
            menuMaterias = input()
    else:
        print('Seleccion inavalida')
    verMenu()
    menu = input()
       


