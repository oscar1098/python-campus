'''
Ejercicio 1Permalink

Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
'''
def esMultiplo(num1,num2):
    num1 = float(input('Ingrese numero 1 '))
    num2 = float(input('Ingrese numero 2 '))
    if num1 % num2 == 0:
        print(num2,' es multiplo de ',num1)
    elif num2 % num1 == 0:
        print(num1,' es multiplo de ',num2)

esMultiplo(8,2)





