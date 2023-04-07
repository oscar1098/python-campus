'''
Para un concierto hay 3 tipos de boletas, desarrollar un programa que calcule el total de ventas de cada boleta (cuantas boltas se vendieron de cada tipo y cuento se recaudo por boleta).
En cada venta se pueden vender mas de una boleta, pero solo de un mismo tipo

    Ubiacion    Valor US$
1   General     50
2   VIP         75
3   Platunium   100 
'''
print('C\n')
op = True

arreglo = [[0.0,0.0],[0.0,0.0],[0.0,0.0]]

def calcular(valor,i1,lista):
    y = int(input('\nCuantas boletas quiere comprar '))
    lista[i1][0] += y
    lista[i1][1] += y*valor
    return lista



while op:
    x = input('\nSeleccione cual boleta va a comprar\n1.General 50\n2.VIP 75\n3.Platinium 100\n4.Salir\n')

    if x == '1':
        calcular(50,0,arreglo)
    elif x == '2':
        calcular(75,1,arreglo)
    elif x == '3':
        calcular(75,2,arreglo)
    elif x == '4':
        op = False
    

print('Total de boletas generales: ','\t',arreglo[0][0],'\t', ' total valor vendido','\t',arreglo[0][1])
print('Total de boletas VIP: ','\t','\t',arreglo[1][0],'\t', ' total valor vendido','\t',arreglo[1][1])
print('Total de boletas platinium: ','\t',arreglo[2][0],'\t', ' total valor vendido','\t',arreglo[2][1])
