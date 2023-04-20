import os
'''
2. Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa debe incorporar funciones para: 1. crear el archivo si este no existe, 2. para consultar el teléfono de un cliente, 3. añadir el teléfono de un nuevo cliente y 4. eliminar el teléfono de un cliente. El listado debe estar guardado en el archivo de texto Directorio.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
'''
ruta = './clase 19-04/ejercicio2/txt/numeros.txt'
   
def escribir(texto,ruta):
    with open(ruta,'w') as archivo:
        archivo.write(texto)
    archivo.close()

def leer(ruta):
   with open(ruta,'r') as archivo:
        return archivo.readlines()

def agregar(contenido,ruta):
    with open(ruta,'a') as archivo:
        archivo.write(contenido)
    archivo.close()
        
try :
    leer(ruta)
except FileNotFoundError:
    numeros = 'OSCAR 3157618908\nSANTIAGO 123456789\nCARLOS 987654321'
    escribir(numeros,ruta)

menu = input('Seleccione\n1.Consultar el telefono de un cliente\n2.Añadir telefono de un nuevo cliente\n3.Eliminar un cliente\n5.Salir\n')

while menu != '5':
    match menu:
        case '1':
            os.system('clear')
            lineas = leer(ruta)
            i = len(lineas)
            
            for palabra in range(i):
                print(lineas[palabra].split()[0])

            nombre = input('\nIngrese el nombre del cliente: ').upper()
            for palabra in range(i):
                nom = lineas[palabra].split()[0]
                if nom == nombre:
                    print('\nEl numero es ',lineas[palabra].split()[1])
                    input()
        case '2':
            os.system('clear')
            nombre = input('Ingrese el nombre del cliente ').upper()
            telefono = input('Ingrese el telefono del cliente ')
            linea = '\n' + nombre +' '+ telefono 
            agregar(linea,ruta)
        case '3':
            os.system('clear')
            lineas = leer(ruta)
            i = len(lineas)
            
            for palabra in range(i):
                print(lineas[palabra].split()[0])

            borrar = input('Ingrese el nombre que quiere borrar ').upper()

            j = 0

            for palabra in range(i):
                eliminar =  lineas[palabra].split()[0]
                if eliminar == borrar:
                    j = palabra
            
            lineas.pop(j)

            print(lineas)
            

            print(j)
            input()



    os.system('clear')
    menu = input('Seleccione\n1.Consultar el telefono de un cliente\n2.Añadir telefono de un nuevo cliente\n4.Eliminar un cliente\n5.Salir\n')


            
            
