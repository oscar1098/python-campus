print('\n\n\n')
cont = 0

print('***********LISTA DE COMPRAS Y VENTAS***************\n')

opcion = input('¿Desea crear una lista de compras o calcular el total de ventas?\n1.Compras\n2.Ventas')

if opcion == '1':
    pcto = input('\nIngrese el producto')
    valor = input('\nIngrese el valor: $')
    pcto = pcto + '\t\t\t$' + valor
    total = int(valor)
    cont = cont + 1
    otro = input('\n¿Desa ingresar otro producto?')
    if otro == 's' or otro == 'S':
        pcto  += '\n' + input('Ingrese el producto')
        valor = input('\nIngrese el valor:$')
        pcto += '\t\t\t$' + valor
        total += int(valor)
        cont += 1


print('\n**************TOTAL COMPRAS*****************')
print('\nPRODUCTOS COMPRADOS: ' + str(cont))
print('\nPRODUCTO\t\tVALOR')
print('\nTOTAL: $' + str(total))
print('\n\n\n')