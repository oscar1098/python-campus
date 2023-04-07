'''
2.  Crea una aplicación que nos pida un número por teclado y con una función se lo pasamos
por parámetro para que nos indique si es o no un número primo, debe devolver true si
es primo sino false.
Un número primo es aquel solo puede dividirse entre 1 y si mismo.
Por ejemplo: 25 no es primo, ya que 25 es divisible entre 5, sin embargo, 17 si es primo.
'''



x = int(input('\nIngrese el numero\n'))
primo = []
for i in range(x):
    if x % (i+1) == 0:
        primo.append(i+1)
if len(primo) == 2:
    print(True)
else:
    print(False)











