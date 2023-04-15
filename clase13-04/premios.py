import json
import os

rutaBasico = './clase13-04/json/dicBasico.json'
rutaIntermedio = './clase13-04/json/dicIntermedio.json'
rutaAvanzado = './clase13-04/json/dicAvanzado.json'
rutaTrainer = './clase13-04/json/trainers.json'
menuGeneral = 0
arregloTrainer = ['','','']

def leerJson(ruta):
    with open(ruta,'r') as archivo:
        diccionario = json.load(archivo)
    archivo.close()
    return diccionario

def actualizarJson(ruta,diccionario={}):
    with open(ruta,'w') as archivo:
        json.dump(diccionario,archivo)
    archivo.close()

def generearId(diccionario):
    try:
        id = int(list(diccionario.keys())[-1])+1
        return id
    except IndexError:
        id = 1
        return id

def menu():
    os.system('clear')
    print('Seleccione:\n1.Registrar Campers\n2.Registrar Expert Trainer\n3.Mostrar campers por grupo\n4.Mostar campers de mayor y menor edad\n5.Salir\n')
    menuGeneral = input()
    return menuGeneral

def menuRegistrarCampers():
    os.system('clear')
    print('*********************REGISTRAR CAMPERS*********************')
    print('Seleccione a que grupo desea añadir campers:\n1.Basico\n2.Intermedio\n3.Avanzado\n4.Salir')
    menuRegistrarCampers = input()
    return menuRegistrarCampers
    
def registrarCampers(team,id,diccionario,numero,ruta):
    os.system('clear')
    print('Cuantos estudiantes desea agregar al grupo',team)
    totalGrupo = int(input())

    for i in range(totalGrupo):
        nombre = input('\nIngrese el nombre ')
        mesIngreso = input('Ingrese la fecha (Ejempo: Enero) ')
        edad = input('Ingrese la edad ')
        diccionario[id]={
            'nombre' : nombre,
            'mesIngreso' : mesIngreso,
            'grupo' : team,
            'edad' : edad
        }
        id +=1
    match numero:
        case 1:
            actualizarJson(ruta,diccionario)
        case 2:
            actualizarJson(ruta,diccionario)
        case 3:
            actualizarJson(ruta,diccionario)

def registrarTrainer():
    os.system('clear')
    print('*********************REGISTRAR EXPERT TRAINER*********************')
    print('\nSeleccione:\n1.Expert trainer grupo basico\n2.Expert trainer grupo intermedio\n3.Expert trainer grupo avanzado')
    trainer = input()
    return trainer

def mostrarEstudiante(diccionario,arreglo,i):
    os.system('clear')
    print('El trainer del grupo es ',arreglo[i],'\n')
    print('ESTUDIANTE\t\tMES DE INGRESO\t\tEDAD\n')
    for estudiante in diccionario:
        print(diccionario[estudiante]['nombre'],'\t\t',diccionario[estudiante]['mesIngreso'],'\t\t\t',diccionario[estudiante]['edad'])

def mayorEdadMenorEdad(diccionario):
    mayor = ['0','']
    menor = ['100','']
    for estudiante in diccionario:
        if int(diccionario[estudiante]['edad']) > int(mayor[0]):
            mayor[0] = diccionario[estudiante]['edad']
            mayor[1] = diccionario[estudiante]['nombre']
        if int(diccionario[estudiante]['edad']) < int(menor[0]):
            menor[0] = diccionario[estudiante]['edad']
            menor[1] = diccionario[estudiante]['nombre']
    mayorMenorEdad = [mayor,menor]
    return mayorMenorEdad

try : 
    leerJson(rutaBasico)
except FileNotFoundError:
    actualizarJson(rutaBasico)

try : 
    leerJson(rutaIntermedio)
except FileNotFoundError:
    actualizarJson(rutaIntermedio)

try : 
    leerJson(rutaAvanzado)
except FileNotFoundError:
    actualizarJson(rutaAvanzado)

try:
    leerJson(rutaTrainer)
except FileExistsError:
    actualizarJson(rutaTrainer,arregloTrainer)
    
menuGeneral = menu() 

while menuGeneral != '5':
    match menuGeneral:
        case '1':
            menuRegisCampers = menuRegistrarCampers()
            while menuRegisCampers != '4':
                match menuRegisCampers:
                    case '1':
                        diccionarioBasico = leerJson(rutaBasico)
                        id = generearId(diccionarioBasico)
                        registrarCampers('Basico',id,diccionarioBasico,1,rutaBasico)
                    case '2':
                        diccionarioIntermedio = leerJson(rutaIntermedio)
                        id = generearId(diccionarioIntermedio)
                        registrarCampers('Intermedio',id,diccionarioIntermedio,2,rutaIntermedio)
                    case '3':
                        diccionarioAvanzado = leerJson(rutaAvanzado)
                        id = generearId(diccionarioAvanzado)
                        registrarCampers('Avanzado',id,diccionarioAvanzado,3,rutaAvanzado)
                    case other:
                        print('Seleccion Invalida')
                menuRegisCampers = menuRegistrarCampers()
        case '2':
            trainerMenu = registrarTrainer()
            match trainerMenu:
                case '1':
                    arregloTrainer = leerJson(rutaTrainer) 
                    trainerBasico = input('Ingrese el nombre del trainer Basico ')
                    arregloTrainer[0] = trainerBasico
                    actualizarJson(rutaTrainer,arregloTrainer)
                case '2': 
                    arregloTrainer = leerJson(rutaTrainer)
                    trainerIntermedio = input('Ingrese el nombre del trainer Intermedio ')
                    arregloTrainer[1] = trainerIntermedio
                    actualizarJson(rutaTrainer,arregloTrainer)
                case '3': 
                    arregloTrainer = leerJson(rutaTrainer)
                    trainerAvanzado = input('Ingrese el nombre del trainer avanzado ')
                    arregloTrainer[2] = trainerAvanzado
                    actualizarJson(rutaTrainer,arregloTrainer)
                
        case '3':
            os.system('clear')
            print('*********************LISTAR CAMPERS*********************')
            mostrar = input('Seleccione\n1.Grupo basico\n2.Grupo intermedio\n3.Grupo avanzado ')
            match mostrar:
                case '1':
                    diccionario = leerJson(rutaBasico)
                    trainer = leerJson(rutaTrainer)
                    mostrarEstudiante(diccionario,trainer,0)
                    input()
                case '2':
                    diccionario = leerJson(rutaIntermedio)
                    trainer = leerJson(rutaTrainer)
                    mostrarEstudiante(diccionario,trainer,1)
                    input()
                case '3':
                    diccionario = leerJson(rutaAvanzado)
                    trainer = leerJson(rutaTrainer)
                    mostrarEstudiante(diccionario,trainer,2)
                    input()

        case '4':
            os.system('clear')
            print('*********************MOSTRAR CAMPERS DE MAYOR Y MENOR EDAD*********************')
            grupo = input('Seleccione\n1.Grupo basico\n2.Grupo intermedio\n3.Grupo avanzado\n ')
            match grupo:
                case '1':
                    diccionarioBasico = leerJson(rutaBasico)
                    edades = mayorEdadMenorEdad(diccionarioBasico)
                    os.system('clear')
                    print('Estudiante de mayor edad ',edades[0][1],'con ',edades[0][0],' años')
                    print('Estudiante de menor edad ',edades[1][1],'con ',edades[1][0],' años')
                    input()
                case '2':
                    diccionarioIntermedio = leerJson(rutaIntermedio)
                    edades = mayorEdadMenorEdad(diccionarioIntermedio)
                    os.system('clear')
                    print('Estudiante de mayor edad ',edades[0][1],'con ',edades[0][0],' años')
                    print('Estudiante de menor edad ',edades[1][1],'con ',edades[1][0],' años')
                    input()
                case '3':
                    diccionarioAvanzado = leerJson(rutaAvanzado)
                    edades = mayorEdadMenorEdad(rutaAvanzado)
                    os.system('clear')
                    print('Estudiante de mayor edad ',edades[0][1],'con ',edades[0][0],' años')
                    print('Estudiante de menor edad ',edades[1][0],'con ',edades[1][1],' años')
                    input()
        case other:
            print('Opcion invalida')
    menuGeneral = menu()




