import random
'''
Determinar en los meses de abril, mayo y junio el promedio de lluvias del mes, teniendo en cuenta los centimetros de lluvia caidos por dia (los valores de los cms de lluvia por dia pueden ser generados por medio de un numero aleatorio entre 0 y 11) y determinar cual fue el mes mas lluvioso en promedio
'''
print('prueba repositorio')

abril = []
mayo = []
junio = []

conta = 0
contm = 0
contj = 0

for i in range(30):
    abril.append(random.randrange(0, 11, 1))
    junio.append(random.randrange(0, 11, 1))

for i in range(31):
    mayo.append(random.randrange(0, 11, 1))

for i in abril:
    conta += i
conta = conta/30

for i in mayo:
    contm += i
contm = contm/31

for i in junio:
    contj += i
contj = contj/30


if conta > contj and conta > contm:
    print('El mes mas lluvioso en promedio fue abril con: ', conta)
elif contm > conta and contm > contj:
    print('El mes mas lluvioso en promedio fue mayo con: ', contm)
else:
    print('El mes mas lluvioso en promedio fue junio con: ', contj)







