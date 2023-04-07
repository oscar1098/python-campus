'''
Dada una lista con nombres completos de personas, realizar un programa que
genere una segunda con la cantidad de palabras de cada uno de los nombres. La
lista de nombres debe llenarse a través de nombres que se ingresan por teclado,
hasta que el nombre ingresado sea “FIN”
Se debe imprimir la lista de nombres y la lista con la cantidad de palabras de cada
nombre.
'''

listaNombres = []
listaCantidadPersonas = []
cont = 0

bucle = True

while bucle:
    texto = input('Ingrese su nombre completo ')
    if texto == 'FIN':
        bucle = False
    else:
        listaNombres.append(texto)
        numeroPalabras = len(listaNombres[cont].split())
        listaCantidadPersonas.append(numeroPalabras)
        cont +=1

for i in range(cont):
    print(listaNombres[i],' tiene ', listaCantidadPersonas[i],' palabras')












