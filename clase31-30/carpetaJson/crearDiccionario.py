import json

#Estructura de datos (diccionario)
diccionario = {
    1: 'Lapiz',
    2: 'Borrador',
    3: 'Cuaderno',
    4: 'Lapicero',
}

#Fase de apertura y creacion
with open('./carpetaJson/json/diccionario.json','w') as archivo:
    json.dump(diccionario,archivo)
            
#Fase de cierre
archivo.close()

x = float(input('x'))

