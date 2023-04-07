'''
Se desea realizar un programa en el cual se ingresen números enteros, los cuales
se deben almacenar en una lista. Se debe ingresar números hasta que el número
ingresado sea 99999. Una vez creada la lista, se desea conocer cuales y cuántos
son pares e impares.
'''
lista =[]
bucle = True
numPar = 0
numImpar = 0

while bucle:
    x = int(input('\nIngrese un numero '))
    lista.append(x)
    if x == 99999:
        bucle = False

for i in lista:
    x = i % 2
    if x == 0:
        numPar +=1
    else:
        numImpar +=1


print(lista)
print('Hay',numPar,' numeros pares')
print('Hay',numImpar,' numeros impares')