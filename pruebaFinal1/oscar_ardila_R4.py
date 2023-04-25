import json
import os
from tabulate import tabulate

ruta = './pruebaFinal1/json/petShopping.json'

def lecturaJson():
    with open(ruta,'r') as archivo:
        tienda = json.load(archivo)
    archivo.close()
    return tienda

def crearJson(tienda):
    with open(ruta,'w') as archivo:
        json.dump(tienda,archivo)
    archivo.close()

def menuGeneral():
    os.system('clear')
    menuGene = input('Seleccione:\n1.Ver mascotas\n2.Crear nueva mascota\n3.Ver mascotas por tipo\n4.Actializar mascotas\n5.Eliminar mascota\n6.Salir\n-')
    return menuGene

def tituloMenu(opcion):
    os.system('clear')
    print(f'-----------------------------------------------------------------------------------{opcion}-----------------------------------------------------------------------------------\n')

def verArregloServicios(arreglo):
    if type(arreglo) == str:
        return arreglo
    else:
        texto = ''
        for servicio in arreglo:
            texto += servicio + ',' + ' '
        return texto

def verMascotas():
    os.system('clear')
    tienda = lecturaJson()
    arregloImprimir = []
    for i in range(len(tienda["petstore"]["pet"])):
        indice = i
        tipo = tienda["petstore"]["pet"][i]["tipo"]
        raza = tienda["petstore"]["pet"][i]["raza"]
        precio = tienda["petstore"]["pet"][i]["precio"]
        servicios = verArregloServicios(tienda["petstore"]["pet"][i]["servicios"])
        imprimir = [indice,tipo,raza,precio,servicios]
        arregloImprimir.append(imprimir)
    print(tabulate(arregloImprimir,headers=['Codigo','Tipo','Raza','Precio','Servicios']))

def crearServicio():
    numeroSer = int(input('\nIngrese el numero de servicios: '))
    if numeroSer == 1:
        servicio = input('\nIngrese el servicio: ')
        return servicio
    else:
        arregloServicio = []
        for i in range(numeroSer):
            servicio = input('\nIngrese el servicio: ')
            arregloServicio.append(servicio)
        return arregloServicio

def verMascotasEditar(i):
    os.system('clear')
    arregloImprimir = []
    tienda = lecturaJson()
    indice = i
    tipo = tienda["petstore"]["pet"][i]["tipo"]
    raza = tienda["petstore"]["pet"][i]["raza"]
    precio = tienda["petstore"]["pet"][i]["precio"]
    servicios = verArregloServicios(tienda["petstore"]["pet"][i]["servicios"])
    imprimir = [indice,tipo,raza,precio,servicios]
    arregloImprimir.append(imprimir)
    print(tabulate(arregloImprimir,headers=['Codigo','Tipo','Raza','Precio','Servicios']))


menuGene = menuGeneral()

while menuGene != '6':
    match menuGene:
        case '1':
            verMascotas()
            input('\nPresione enter para continuar')
        case '2':
            tituloMenu('CREAR MASCOTA')
            tienda = lecturaJson()
            tipo = input('Ingrese el tipo de mascota: ')
            raza = input('Ingrese la raza de la mascota: ')
            talla = input('Ingrese la talla de la mascota: ')
            precio = input('Ingrese el precio de la mascota: ')
            servicio = crearServicio()
            dicc = {"tipo":tipo,"raza": raza,"talla": talla,"precio" : precio,"servicios":servicio}
            tienda["petstore"]["pet"].append(dicc)
            crearJson(tienda)
            input('\nMascota creada correctamente presione enter para continuar')
        case '3':
            tituloMenu('MASCOTAS P0R TIPO')
            tienda = lecturaJson()
            arregloImprimir= []
            for i in range(len(tienda["petstore"]["pet"])):
                id = i
                tipo = tienda["petstore"]["pet"][i]["tipo"]
                arreglo = [id,tipo]
                arregloImprimir.append(arreglo)
            print(tabulate(arregloImprimir,headers=['Codigo','Tipo']))
            codigo = int(input('\nIngrese el codigo del tipo de la mascota que desea ver: '))
            tipo = tienda["petstore"]["pet"][codigo]["tipo"]
            arregloImprimir= []
            for i in range(len(tienda["petstore"]["pet"])):

                if tienda["petstore"]["pet"][i]["tipo"] == tipo:
                    id = i
                    raza = tienda["petstore"]["pet"][i]["raza"]
                    precio = tienda["petstore"]["pet"][i]["precio"]
                    servicio = verArregloServicios(tienda["petstore"]["pet"][i]["servicios"])
                    arreglo = [id,raza,precio,servicio]
                    arregloImprimir.append(arreglo)
            os.system('clear')
            print(tabulate(arregloImprimir,headers=['Codigo','Raza','Precio','servicio']))
            input('\nPresione enter para continuar')
        case '4':
            tituloMenu('ACTUALIZAR MASCOTAS')
            verMascotas()
            tienda = lecturaJson()
            codigo = int(input('\nIngrese el codigo de la mascota que desea actualizar: '))
            verMascotasEditar(codigo)
            menuEditar = input('\nSeleccione:\n1.Editar tipo\n2.Editar raza\n3.Editar talla\n4.Editar precio\n5.Editar servicios\n-')
            match menuEditar:
                case '1':
                    tienda["petstore"]["pet"][codigo]["tipo"] = input('\nIngrese el nuevo tipo: ')
                case '2':
                    tienda["petstore"]["pet"][codigo]["raza"] = input('\nIngrese la nueva raza: ')
                case '3':
                    tienda["petstore"]["pet"][codigo]["talla"] = input('\nIngrese la nueva talla: ')
                case '4':
                    tienda["petstore"]["pet"][codigo]["precio"] = input('\nIngrese el nuevo precio: ')
                case '5':
                    tienda["petstore"]["pet"][codigo]["servicios"] = crearServicio()
            crearJson(tienda)
            input('\nSe actualizo correctamente presione enter para continuar')
        case '5':
            tituloMenu('ELIMINAR MASCOTAS')
            verMascotas()
            tienda = lecturaJson()
            codigo = int(input('\nIngrese el codigo de la mascota que desea borrar: '))
            tienda["petstore"]["pet"].pop(codigo)
            crearJson(tienda)
            input('\nSe elimino correctamente presione enter para continuar')
        case other:
            print('Seleccion invalida')
    menuGene = menuGeneral()
           

