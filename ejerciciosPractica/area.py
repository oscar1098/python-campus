import math

print('Ingrese:\n1 para hallar el area de un circulo\n2 para hallar el area de un cuadrado\n3 para hallar el area de un triangulo\n4 para hallar el area de un trapecio\n5 para hallar el area de un paralelogramo')

x = int(input(':)_'))

if x == 1:
    y = int(input('Ingrese el valor del radio: '))
    print('El area del circulo es, ', (math.pi)*(y**2))
elif x == 2:
    y = int(input('Ingrese el valor del lado: '))
    print('El area del cuadrado es: ', y*y)
elif x == 3:
    base = int(input('Ingrese el valor de la base '))
    altura = int(input('Ingrese el valor de la alrtura '))
    print('El area del triangulo es: ', (base*altura)/2)
elif x == 4:
    baseMenor = int(input('Ingrese la base menor: '))
    baseMayor = int(input('Ingrese la base mayor: '))
    altura = int(input('Ingrese la altura: '))
    area = ((baseMenor+baseMayor)*altura)/2
    print('El area del trapecio es: ', area)
elif x == 5:
    base = int(input('Ingrese el valor de la base: '))
    altura = int(input('Ingrese el valor de la altura: '))
    print('El area del paralelogramo es: ', base*altura)
