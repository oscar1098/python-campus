import json
import os

ruta = './clase 20-04/ejercicio1/json/empresa.json'
empresas = {'personas':[]}
arregloMax = []

def leer(ruta):
    with open(ruta,'r') as archivo:
        diccionario = json.load(archivo)
    archivo.close()
    return diccionario

def escribir(ruta,diccionario = empresas):
    with open(ruta,'w') as archivo:
        json.dump(diccionario,archivo)
    archivo.close()

def menuGeneral():
    menu = input('Seleccione\n1.Agregar\n2.Mostrar\n3.Editar\n4.Eliminar\n5.Salir\n')
    return menu
 
try:
    leer(ruta)
except FileNotFoundError:
    escribir(ruta)

menu = menuGeneral()

while menu != '5':
    match menu:
        case '1':
            nombre = input('Ingrese un nombre ')
            edad = input('Ingrese la edad ')
            documento = input('Numero documento ')

            empresa = leer(ruta)

            if len(empresa['personas']) == 0:
                id = 1
            else :
                for i in range(len(empresa['personas'])):
                    arregloMax.append(empresa['personas'][i]['id'])
                id = max(arregloMax) + 1

            dicc = {
                'id': id,
                'nombre': nombre,
                'edad': edad,
                'documento': documento
            }

            empresa['personas'].append(dicc)

            escribir(ruta,empresa)
        case '2':


    



