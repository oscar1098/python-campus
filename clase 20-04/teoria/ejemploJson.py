import json

ruta = './clase 20-04/json/json.json'

lista = {1: 'Lapiz',2:'Borrador',3:'Cuaderno',4:'Lapicero'}

with open(ruta,'w') as archivo:
    json.dump(lista,archivo)
archivo.close()

with open(ruta,'r') as archivo:
    diccionario = json.load(archivo)
