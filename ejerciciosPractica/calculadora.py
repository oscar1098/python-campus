
print('Ingrese:\nS para suma\nR pararesta\nM para multiplicacion\nD para Division')
x = input(':)_')

if x == 'S' or x == 's':
    num1 = int(input('Ingrese el numero 1 '))
    num2 = int(input('Ingrese el numero 2 '))
    print(num1+num2)
elif x == 'r' or x == 'R':
    num1 = int(input('Ingrese el numero 1 (minuendo) '))
    num2 = int(input('Ingrese el numero 2 (substraendo) '))
    print(num1-num2)
elif x == 'M' or x == 'm':
    num1 = int(input('Ingrese el numero 1 '))
    num2 = int(input('Ingrese el numero 2 '))
    print(num1*num2)
elif x == 'D' or x == 'd':
    num1 = int(input('Ingrese el numero 1 (dividendo) '))
    num2 = int(input('Ingrese el numero 2 (divisor) '))
    if num2 == 0:
        print('El divisor no puede ser igual a cero ')
    else :
        print(num1/num2)
       



