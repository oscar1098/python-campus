import json


#Fase de apertura y creacion
with open('./carpetaJson/json/lista.json','r') as archivo:
    lista = json.load(archivo)
            
#Fase de cierre
archivo.close()

print('Lista: ', lista)

for i in lista:
    print(i)