edad = int(input('Ingrese su edad: '))

if edad < 2:
    print('Bebe')
elif edad <= 11:
    print('Niño')
elif edad <= 17:
    print('Adolecente')
elif edad == 18:
    print('mayor de edad')
elif edad <= 35:
    print('Adulto Joven')
elif edad <= 55:
    print('Mediana edad')
elif edad <= 90:
    print('Adulto mayor')
elif edad <= 110:
    print('TE')
