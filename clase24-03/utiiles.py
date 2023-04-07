'''
Se realiza la compra de N artículos, en donde se ingresa el código del artículo y la cantidad y
mediante el uso de diccionarios para los nombres y valores unitarios de los artículos, el
programa debe obtener el nombre de cada artículo, cantidad comprada, valor unitario, valor
total de acuerdo a la cantidad comprada y finalmente calcular el valor total de la compra.
Se suministra el diccionario de nombres de artículo y otro con los valores unitarios.
articulos={1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores={1:2500,2:3800,3:1200,4:35000,5:3700}
'''

articuloscomprados = 0
totalVentaProducto = 0
indiceArticulo = 0
totalVenta = 0
msj = ''
compra = True

articulos = {
    1: 'Lapiz',
    2: 'Cuadernos',
    3: 'Borrador',
    4: 'Calculadora',
    5: 'Escuadra'
}

valores = {
    1: 2500,
    2: 3800,
    3: 1200,
    4: 35000,
    5: 3700
}

while compra:

    indiceArticulo = int(input('Ingrese el articulo que desea comprar:\n1.Lapiz,\n2.Cuadernos\n3.Borrador\n4.Calculadora\n5.Escuadra\n6.Salir\n'))

    if indiceArticulo == 6:
        compra = False
    else: 
        
        articuloscomprados = int(input('Ingrese cuantos articulos desea comrprar\n'))

        totalVentaProducto = valores[indiceArticulo]*articuloscomprados

        totalVenta += totalVentaProducto 

        msj += '\nNombre del articulo: ' + articulos[indiceArticulo] +'\n'+ 'Cantida comprada: ' + str(articuloscomprados) + '\n'+ 'Valor unitario de ' + articulos[indiceArticulo] +'= ' + str(valores[indiceArticulo]) + '\n' + 'Valor total de ' + articulos[indiceArticulo] + ' comprados '+ str(totalVentaProducto) + '\n\n'
    
print(msj)
print('\nTotal de la compra: ', totalVenta)






