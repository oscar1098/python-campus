import json

#Estructura de datos (lista)
lista = [10,20,30,40,50,60]

#Fase de apertura y creacion
with open('./carpetaJson/json/lista.json','w') as archivo:
    json.dump(lista,archivo)
              
archivo.close()

