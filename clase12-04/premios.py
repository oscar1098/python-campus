import json
import os
'''
1. Crear grupos Básicos, Intermedio y avanzados con campers y
sus datos personales (Nombre, Mes de Ingreso, Grupo y Edad.
1.1 Registrar Expert Trainer Del grupo Básico.
1.4 Listar los Campers del grupo
1.7 Reportar los campers de mayor y menor edad de cada grupo
'''
rutaBasico = './clase12-04/json/dicBasico.json'
rutaIntermedio = './clase12-04/json/dicIntermedio.json'
rutaAvanzado = './clase12-04/json/dicAvanzado.json'
menuGeneral = 0

def leerDiccBasico(ruta):
    with open(ruta,'r') as archivo:
        dicBasico = json.load(archivo)
    archivo.close()
    return dicBasico

def leerDiccIntermedio(ruta):
    with open(ruta,'r') as archivo:
        dicIntermedio = json.load(archivo)
    archivo.close()
    return dicIntermedio

def leerDiccvanzado(ruta):
    with open(ruta,'r') as archivo:
        dicAvanzado = json.load(archivo)
    archivo.close()
    return dicAvanzado

def actualizarDiccBasico(ruta,diccionario):
    with open(ruta,'w') as archivo:
        json.dump(diccionario,archivo)
    archivo.close()

def actualizarDiccIntermedio(ruta,diccionario):
    with open(ruta,'w') as archivo:
        json.dump(diccionario,archivo)
    archivo.close()

def actualizarDiccAvanzado(ruta,diccionario):
    with open(ruta,'w') as archivo:
        json.dump(diccionario,archivo)
    archivo.close()

def generarid(diccionario):
    id = int(list(diccionario.keys())[-1])+1
    return id


def menu():
    os.system('clear')
    print('Seleccione:\n1.Registrar Campers\n2.Registrar Expert Trainer\n3.Mostrar campers por grupo\n4.Mostar campers de mayor y menor edad\n5.Salir\n')
    menuGeneral = input()
    return menuGeneral

def menuRegistrarCampers():
    os.system('clear')
    print('*********************REGISTRAR CAMPERS*********************')
    print('Seleccione a que grupo desea añadir campers:\n1.Basico\n2.Intermedio\n3.Avanzado\n')
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
        match numero:
            case 1:
                actualizarDiccBasico(ruta,diccionario)
            case 2:
                actualizarDiccIntermedio(ruta,diccionario)
            case 3:
                actualizarDiccAvanzado(ruta,diccionario)

try : 
    leerDiccBasico(rutaBasico)
except FileNotFoundError:
    with open(rutaBasico,'w') as archivo:
        diccBasico = {1:{}}
        json.dump(diccBasico,archivo)
    archivo.close()


menuGeneral = menu() 

while menuGeneral != '5':
    match menuGeneral:
        case '1':
            menuRegisCampers = menuRegistrarCampers()
            match menuRegisCampers:
                case '1':
                    diccionarioBasico = leerDiccBasico(rutaBasico)
                    id = generarid(diccionarioBasico)
                    registrarCampers('Basico',id,diccionarioBasico,1,rutaBasico)
                case '2':
                    diccionarioIntermedio = leerDiccIntermedio(rutaIntermedio)
                    id = generarid(diccionarioIntermedio)
                    registrarCampers('Intermedio',id,diccionarioIntermedio,2,rutaIntermedio)
                case '3':
                    diccionarioAvanzado = leerDiccvanzado(rutaAvanzado)
                    id = generarid(diccionarioAvanzado)
                    registrarCampers('Avanzado',id,diccionarioAvanzado,3,rutaAvanzado)

                    

            
        case '2':
            print('*********************REGISTRAR EXPERT TRAINER*********************')
            input()
        case '3':
            print('*********************LISTAR TRAINERS*********************')
            input()
        case '4':
            print('*********************MOSTRAR CAMPERS DE MAYOR Y MENOR EDAD*********************') 
            input()
        case other:
            print('Opcion invalida')
    menuGeneral = menu()

    



