op = True
conts = 0
contr = 0
contm = 0
contd = 0

while op:

    print('Ingrese:\nS para suma\nR pararesta\nM para multiplicacion\nD para Division')
    x = input(':)_')

    if x == 'S' or x == 's':
        conts +=1
        num1 = int(input('Ingrese el numero 1 '))
        num2 = int(input('Ingrese el numero 2 '))
        print(num1+num2)
        x = input('s para salir')
        if x == 's':
            op = False
    elif x == 'r' or x == 'R':
        contr +=1
        num1 = int(input('Ingrese el numero 1 (minuendo) '))
        num2 = int(input('Ingrese el numero 2 (substraendo) '))
        print(num1-num2)
        x = input('s para salir')
        if x == 's':
            op = False
    elif x == 'M' or x == 'm':
        contm +=1
        num1 = int(input('Ingrese el numero 1 '))
        num2 = int(input('Ingrese el numero 2 '))
        print(num1*num2)
        x = input('s para salir')
        if x == 's':
            op = False
    elif x == 'D' or x == 'd':
        contd +=1
        num1 = int(input('Ingrese el numero 1 (dividendo) '))
        num2 = int(input('Ingrese el numero 2 (divisor) '))
        if num2 == 0:
            print('El divisor no puede ser igual a cero ')
        else :
            print(num1/num2)
        x = input('s para salir')
        if x == 's':
            op = False
       

print('\nHizo en total ',conts,' sumas')
print('Hizo en total ',contr,' restas')
print('Hizo en total ',contm,' multiplicaciones')
print('Hizo en total ',contd,' divisiones')

