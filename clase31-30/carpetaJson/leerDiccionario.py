import json


#Fase de apertura y creacion
with open('./carpetaJson/json/diccionario.json','r') as archivo:
    diccionario = json.load(archivo)
            
#Fase de cierre
archivo.close()

print('Diccionario: ', diccionario)

for i in diccionario:
    print(i)
print(diccionario['1'])

