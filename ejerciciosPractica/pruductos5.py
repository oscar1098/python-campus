print('\n\n\n')
cont = 0
pcto = ''
cont2 = 0
pcto2 = ''
contv = 0
cont3 = 0
op = True



print('***********LISTA DE COMPRAS Y VENTAS***************\n')


while op:
    opcion = input('\n¿Desea crear una lista de compras o calcular el total de ventas?\n1.Compras\n2.Ventas ')
    if opcion == '1':
        valor = input('Ingrese el valor del producto ')
        pcto +=   input('Ingrese el nombre del producto ')+'\t\t\t' + valor + '\n'
        cont += 1
        cont2 = cont2 + int(valor)
        x = input('para salir s')
        if x == 's':
            op = False
    if opcion == '2':
        valor2 = input('Ingrese el valor del producto ')
        pcto2 +=   input('Ingrese el nombre del producto ')+'\t\t\t' + valor2 + '\n'
        contv += 1
        cont3 = cont3 + int(valor2)
        x = input('para salir s')
        if x == 's':
            op = False


print('VENTAS\n')
print('\nVALOR\t\tPRODUCTO')
print(pcto)
print('total de productos: '+ str(cont))
print('\nValor total de la compra',cont2,)
print('\n--------------------------------------------------\n')

print('COMPRAS\n')
print('\nVALOR\t\tPRODUCTO')
print(pcto2)
print('total de productos: '+ str(contv))
print('\nValor total de la compra',cont3)

