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
bolGen = 0
totGen = 0
bolVip = 0
totVip = 0
bolPlat = 0
totPlat = 0

while op:
    x = input('\nSeleccione cual boleta va a comprar\n1.General 50\n2.VIP 75\n3.Platinium 100\n4.Salir\n')

    if x == '1':
        y = int(input('\nCuantas boletas quiere comprar '))
        totGen += y*50
        bolGen += y
    elif x == '2':
        y = int(input('\nCuantas boletas quiere comprar '))
        totVip += y*75
        bolVip += y
    elif x == '3':
        y = int(input('\nCuantas boletas quiere comprar '))
        totPlat += y*100
        bolPlat += y
    elif x == '4':
        op = False
    

print('Total de boletas generales: ','\t',bolGen,'\t', ' total valor vendido','\t',totGen)
print('Total de boletas VIP: ','\t','\t',bolVip,'\t', ' total valor vendido','\t',totVip)
print('Total de boletas platinium: ','\t',bolPlat,'\t', ' total valor vendido','\t',totPlat)
