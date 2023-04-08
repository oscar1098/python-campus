import json
import os

id = 1
pathEstu = './ejerciciosPractica/Ejercicio notas/json/dicEstudiantes.json'
pathMate = './ejerciciosPractica/Ejercicio notas/json/dicMaterias.json'
pathNota = './ejerciciosPractica/Ejercicio notas/json/dicNotas.json'
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



def leerDicEstu():
    with open(pathEstu,'r') as archivo:
        leerDicEstu = json.load(archivo)
    archivo.close()
    return leerDicEstu

def leerDicMate():
    with open(pathMate,'r') as archivo:
        leerdicMate = json.load(archivo)
    archivo.close()
    return leerdicMate

def leerDicNota():
    with open(pathNota,'r') as archivo:
        dicNota = json.load(archivo)
    archivo.close()
    return dicNota

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
    dicMate = leerDicMate()
    print('CODIG0\t\t MATERIA')
    for materia in dicMate:
        print(materia,'\t\t',dicMate[materia]['nombre'])

def verMenuEstudiantes():
    os.system('clear')
    print('*********************ESTUDIANTES*********************')
    print('Seleccione:\n1.Ver estudiantes\n2.Agregar\n3.Editar\n4.Eliminar\n0.Salir')

def verEstudiantes():
    dicEstu = leerDicEstu()
    print('CODIGO\t\t NOMBRE\t\t APELLIDO\t\t CORREO')
    for estudiante in dicEstu:
        print(estudiante,'\t\t',dicEstu[estudiante]['nombre'],'\t\t',dicEstu[estudiante]['apellido'],'\t\t',dicEstu[estudiante]['correo'])

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
    dicEstu = leerDicEstu()
    with open(pathEstu,'w') as archivo:
        dicEstu[id][itemCambio] = nuevoValor
        json.dump(dicEstu,archivo)
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
    dicMate = leerDicMate()
    dicEstu = leerDicEstu()
    dicNota = leerDicNota()

    print('Notas de los estudiantes en la materia',dicMate[id]['nombre'])
    print('CODIGO\t\t NOMBRE\t\t NOTA 1\t\t NOTA 2\t\t NOTA 3\t\t NOTA FINAL\t\t')
    for nota in dicNota:
        if dicNota[nota]['idMateria'] == id:
            idEs = dicNota[nota]['idEstudiante']
            print(nota,'\t\t',dicEstu[idEs]['nombre'],'\t\t',dicNota[nota]['nota1'],'\t\t',dicNota[nota]['nota2'],'\t\t',dicNota[nota]['nota3'],'\t\t',dicNota[nota]['notaFinal'])

def verNotaEstu():
    os.system('clear')
    verEstudiantes()
    id = input('Ingrese el codigo del estudiante ')
    os.system('clear')
    dicMate = leerDicMate()
    dicEstu = leerDicEstu()
    dicNotas = leerDicNota()
    
    print('Notas de las materias del estudiante',dicEstu[id]['nombre'])
    print('CODIGO\t\t MATERIA\t\t NOTA 1\t\t NOTA 2\t\t NOTA 3\t\t NOTA FINAL\t\t')
    for nota in dicNotas:
        if dicNotas[nota]['idEstudiante'] == id:
            idMa = dicNotas[nota]['idMateria']
            print(nota,'\t\t',dicMate[idMa]['nombre'],'\t\t',dicNotas[nota]['nota1'],'\t\t',dicNotas[nota]['nota2'],'\t\t',dicNotas[nota]['nota3'],'\t\t',dicNotas[nota]['notaFinal'])

def editarNotas(id,leerNotas,nota):
    n = float(input('Ingrese la nota '))
    with open(pathNota,'w') as archivo:
        leerNotas[id][nota] = n
        json.dump(leerNotas,archivo)
    archivo.close()

def agregarNotas(dicNotas,nota,dicEstu,dicMate,id,notatext):
    idEs = dicNotas[nota]['idEstudiante']
    print('Ingrese la', notatext, ' del estudiante',dicEstu[idEs]['nombre'],'en la materia',dicMate[id]['nombre'])
    nota3 = float(input())
    dicNotas[nota][notatext] = nota3
    return dicNotas

try:
    leerDicEstu()
except FileNotFoundError:
    with open(pathEstu,'w') as archivo:
        json.dump(dicEstudiante,archivo)
    archivo.close()

try:
    leerDicMate()
except FileNotFoundError:
    with open(pathMate,'w') as archivo:
        json.dump(dicMaterias,archivo)
    archivo.close()

try:
    leerDicNota()
except FileNotFoundError:
    with open(pathNota,'w') as archivo:
        json.dump(dicNotas,archivo)
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
            dicNotas = leerDicNota()
            dicMate = leerDicMate()
            dicEstu = leerDicEstu()           
            
            with open(pathNota,'w') as archivo:
                for nota in dicNotas:
                    if dicNotas[nota]['idMateria'] == id:
                        if dicNotas[nota]['nota3'] != 'p':
                            idEs = dicNotas[nota]['idEstudiante']
                            print('Calculando la nota final del estudiante',dicEstu[idEs]['nombre'],'en la materia',dicMate[id]['nombre'])
                            nota3 = dicNotas[nota]['nota3']
                            nota2 = dicNotas[nota]['nota2']
                            nota1 = dicNotas[nota]['nota1']
                            notaFinal = nota1*0.3 + nota2*0.3 + nota3*0.4
                            dicNotas[nota]['notaFinal'] = round(notaFinal,2)
                            input()
                        elif dicNotas[nota]['nota2'] != 'p':
                            dicNotas = agregarNotas(dicNotas,nota,dicEstu,dicMate,id,'nota3')
                        elif dicNotas[nota]['nota1'] != 'p':
                            dicNotas = agregarNotas(dicNotas,nota,dicEstu,dicMate,id,'nota2')
                        elif dicNotas[nota]['nota1'] == 'p':
                            dicNotas = agregarNotas(dicNotas,nota,dicEstu,dicMate,id,'nota1')
                json.dump(dicNotas,archivo)                
            archivo.close()
            input()
        elif menuNota == '3':
            os.system('clear')
            print('*********************EDITAR NOTAS*********************')
            verNotaMateria()
            id = input('\nSeleccione el estudiante del que desea editar las notas ')
            dicNotas = leerDicNota()
            if dicNotas[id]['notaFinal'] =='p':
                print('\nseleccione\n1.Editar nota 1\n2.Editar nota 2\n3.Editar nota 3')
                editarNota = input()
                if editarNota == '1' and dicNotas[id]['nota1'] != 'p':
                    editarNotas(id,dicNotas,'nota1')
                elif editarNota == '2' and dicNotas[id]['nota2'] != 'p':
                    editarNotas(id,dicNotas,'nota2')
                elif editarNota == '3' and dicNotas[id]['nota3'] != 'p':
                    editarNotas(id,dicNotas,'nota3')
                else:
                    print('No se puede editar la nota no hay registro de la nota')
            else:
                print('No se pueden editar las notas ya esta registrada la nota finales')
            input()
        elif menuNota == '4':
            os.system('clear')
            print('*********************ELIMINAR NOTAS*********************')
            print('Seleccione\n1.Eliminar registro de notas\n2.Salir')
            op = input()
            if op == '1':
                dicNotas = leerDicNota()
                with open(pathNota,'w') as archivo:
                    for nota in dicNotas:
                        dicNotas[nota]['nota1'] = 'p'
                        dicNotas[nota]['nota2'] = 'p'
                        dicNotas[nota]['nota3'] = 'p'
                        dicNotas[nota]['notaFinal'] = 'p'
                    json.dump(dicNotas,archivo)
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
                dicEstu = leerDicEstu()
                id = generarID(dicEstu)
                with open(pathEstu,'w') as archivo:
                    dicEstu[id]={'nombre': nombre, 'apellido': apellido, 'correo': correo}   
                    json.dump(dicEstu,archivo)
                archivo.close()
                
                dicMate = leerDicMate()
                dicNotas = leerDicNota()
                idN = int(generarID(dicNotas))
                with open(pathNota,'w') as archivo:
                    for materia in dicMate:
                        cont = 0
                        for nota in dicNotas:
                            if dicNotas[nota]['idMateria'] == materia and dicNotas[nota]['nota1'] == 'p' and cont == 0: 
                                arregloEliminar.append(dicNotas[nota]['idMateria'])
                                cont +=1
                    for materia in arregloEliminar:
                        dicNotas[str(idN)]={
                            'idEstudiante':id,
                            'idMateria': materia,
                            'nota1': 'p',
                            'nota2': 'p',
                            'nota3': 'p',
                            'notaFinal': 'p'
                        }
                        idN += 1
                    arregloEliminar.clear()
                    json.dump(dicNotas,archivo)
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
                
                dicEstu = leerDicEstu()
                with open(pathEstu, 'w') as archivo:
                    del(dicEstu[id])
                    json.dump(dicEstu,archivo)
                archivo.close()

                dicNotas = leerDicNota()
                for estudiante in dicNotas:
                    if dicNotas[estudiante]['idEstudiante'] == id:
                        arregloEliminar.append(estudiante)
                with open(pathNota, 'w') as archivo:
                    for registro in arregloEliminar:
                        del(dicNotas[registro])
                    json.dump(dicNotas,archivo)
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

                dicMate = leerDicMate()
                with open(pathMate,'w') as archivo:
                    id = generarID(dicMate)
                    dicMate[id] = {'nombre' : nombre}
                    json.dump(dicMate,archivo)
                archivo.close()

                dicEstu = leerDicEstu()
                dicMate = leerDicMate()
                dicNotas = leerDicNota()
                id = int(generarID(dicNotas))
                idM = int(generarID(dicMate)) -1
                with open(pathNota,'w') as archivo:
                    for estudiante in dicEstu:
                        dicNotas[str(id)] = {
                            'idEstudiante':estudiante,
                            'idMateria': str(idM),
                            'nota1': 'p',
                            'nota2': 'p',
                            'nota3': 'p',
                            'notaFinal': 'p'
                        }
                        id += 1
                    json.dump(dicNotas,archivo)
                archivo.close()
                input()


            elif menuMaterias == '3':
                os.system('clear')
                print('*********************EDITAR MATERIA*********************')
                verMaterias()

                id = input('Ingrese el id de la materia que desea editar ')
                nombre = input('\nIngrese el nombre de la materia ')

                dicMate = leerDicMate()
                with open(pathMate,'w') as archivo:
                    for materia in dicMate:
                        if materia == id:
                            dicMate[materia]['nombre'] = nombre
                    json.dump(dicMate,archivo)
                archivo.close()
                input()

            elif menuMaterias == '4':
                os.system('clear')
                print('*********************ELIMINAR MATERIA*********************')
                verMaterias()

                id = input('Ingrese el id de la materia que desea eliminar ')

                dicNotas = leerDicNota()
                cont = 0
                for nota in dicNotas:
                    if dicNotas[nota]['idMateria'] == id and dicNotas[nota]['nota1'] != 'p':
                        cont += 1  

                if cont == 0:
                    dicMate = leerDicMate()
                    for nota in dicNotas:
                        if dicNotas[nota]['idMateria'] == id :
                            arregloEliminar.append(nota)
                    with open(pathNota,'w') as archivo:
                        for materia in arregloEliminar:
                            del(dicNotas[materia])
                        json.dump(dicNotas,archivo)
                    archivo.close()
                        
                    with open(pathMate,'w') as archivo:
                        del(dicMate[id])
                        json.dump(dicMate,archivo)
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
       


