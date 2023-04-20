import io

'''
1. Elabore un Programa Python que lea la ruta y nombre de un archivo y muestre por pantalla la línea M del archivo.
La línea a mostrar también debe ser un dato ingresado por el usuario del programa.
Si el archivo no existe debe mostrar un mensaje por pantalla informando de ello.
'''
ruta = './clase 19-04/ejercicio1/txt/tigre.txt'

texto = open(ruta,'r')
linea = texto.readlines()

texto.close()

try :
    lin = int(input('Ingrese la la linea '))
    print(linea[lin-1])
except IndexError:
    print('No existe el indice')
except ValueError:
    print('Digite solo numeros')

