import json
import os

rutaBasico = './clase13-04/json/dicBasico.json'
rutaIntermedio = './clase13-04/json/dicIntermedio.json'
rutaAvanzado = './clase13-04/json/dicAvanzado.json'
rutaTrainer = './clase13-04/json/trainers.json'
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
        return 1

def revisarJson(ruta):
    try : 
        leerJson(ruta)
    except FileNotFoundError:
        actualizarJson(ruta)

def menu():
    os.system('clear')
    menuGeneral = input('Seleccione:\n1.Registrar Campers\n2.Registrar Expert Trainer\n3.Mostrar campers por grupo\n4.Mostar campers de mayor y menor edad\n5.Salir\n')

    return menuGeneral

def menuRegistrarCampers():
    os.system('clear')
    print('*********************REGISTRAR CAMPERS*********************')
    menuRegistrarCampers = input('Seleccione a que grupo desea añadir campers:\n1.Basico\n2.Intermedio\n3.Avanzado\n4.Salir\n')

    return menuRegistrarCampers
    
def registrarCampers(team,ruta):
    os.system('clear')
    print('Cuantos estudiantes desea agregar al grupo\n')
    totalGrupo = int(input())

    diccionario = leerJson(ruta)
    id = generearId(diccionario)

    for i in range(totalGrupo):
        nombre = input('\nIngrese el nombre ')
        mesIngreso = input('Ingrese la fecha (Ejempo: Enero) ')
        edad = input('Ingrese la edad ')
        diccionario[id]={'nombre' : nombre,'mesIngreso' : mesIngreso,'grupo' : team,'edad' : edad}
        id +=1
    actualizarJson(ruta,diccionario)

def menuregistrarTrainer():
    os.system('clear')
    print('*********************REGISTRAR EXPERT TRAINER*********************')
    trainer = input('\nSeleccione:\n1.Expert trainer grupo basico\n2.Expert trainer grupo intermedio\n3.Expert trainer grupo avanzado\n')

    return trainer

def registrarTrainer(i,ruta):
    arregloTrainer = leerJson(ruta) 
    trainer = input('Ingrese el nombre del trainer ')
    arregloTrainer[i] = trainer
    actualizarJson(ruta,arregloTrainer)

def mostrarEstudiante(rutaEstu,rutaTrainer,i):
    os.system('clear')
    diccionario = leerJson(rutaEstu)
    trainer = leerJson(rutaTrainer)
    print('El trainer del grupo es ',trainer[i],'\n')
    print('ESTUDIANTE\t\tMES DE INGRESO\t\tEDAD\n')
    for estudiante in diccionario:
        print(diccionario[estudiante]['nombre'],'\t\t',diccionario[estudiante]['mesIngreso'],'\t\t\t',diccionario[estudiante]['edad'])
    input()

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

def mostrarEdades(ruta):
    diccionario = leerJson(ruta)
    edades = mayorEdadMenorEdad(diccionario)
    os.system('clear')
    print('Estudiante de mayor edad es',edades[0][1],'con ',edades[0][0],' años')
    print('Estudiante de menor edad es',edades[1][1],'con ',edades[1][0],' años')
    input()

revisarJson(rutaBasico)

revisarJson(rutaIntermedio)

revisarJson(rutaAvanzado)

try:
    leerJson(rutaTrainer)
except FileNotFoundError:
    actualizarJson(rutaTrainer,arregloTrainer)
    
menuGeneral = menu() 

while menuGeneral != '5':
    match menuGeneral:
        case '1':
            menuRegisCampers = menuRegistrarCampers()
            while menuRegisCampers != '4':
                match menuRegisCampers:
                    case '1':
                        registrarCampers('Basico',rutaBasico)
                    case '2':
                        registrarCampers('Intermedio',rutaIntermedio)
                    case '3':
                        registrarCampers('Avanzado',rutaAvanzado)
                    case other:
                        print('Seleccion Invalida')
                menuRegisCampers = menuRegistrarCampers()
        case '2':
            trainerMenu = menuregistrarTrainer()
            match trainerMenu:
                case '1':
                    registrarTrainer(0,rutaTrainer)
                case '2': 
                    registrarTrainer(1,rutaTrainer)
                case '3': 
                    registrarTrainer(2,rutaTrainer)
        case '3':
            os.system('clear')
            print('*********************LISTAR CAMPERS*********************')
            mostrar = input('Seleccione\n1.Grupo basico\n2.Grupo intermedio\n3.Grupo avanzado\n')
            match mostrar:
                case '1':
                    mostrarEstudiante(rutaBasico,rutaTrainer,0)
                case '2':
                    mostrarEstudiante(rutaIntermedio,rutaTrainer,1)
                case '3':
                    mostrarEstudiante(rutaAvanzado,rutaTrainer,2)
        case '4':
            os.system('clear')
            print('*********************MOSTRAR CAMPERS DE MAYOR Y MENOR EDAD*********************')
            grupo = input('Seleccione\n1.Grupo basico\n2.Grupo intermedio\n3.Grupo avanzado\n ')
            match grupo:
                case '1':
                    mostrarEdades(rutaBasico)
                case '2':
                    mostrarEdades(rutaIntermedio)
                case '3':
                    mostrarEdades(rutaAvanzado)
        case other:
            print('Opcion invalida')
    menuGeneral = menu()




