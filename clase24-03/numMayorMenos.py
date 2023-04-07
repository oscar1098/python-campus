'''
Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
'''

mayorMenor=[0.0,0.0]

numerosAgregados=[]

numeros = True

def calculaMaxMin(arreglo,arreglo2):

    for i in range(len(arreglo)):
        cont = 0
        for j in arreglo:
            if arreglo[i] > j:
                cont +=1
        if cont == (len(arreglo)-1):
            arreglo2[0] = arreglo[i]
        
    for i in range(len(arreglo)):
        cont = 0
        for j in arreglo:
            if arreglo[i] < j:
                cont +=1
        if cont == (len(arreglo)-1):
            arreglo2[1] = arreglo[i]
    return arreglo2

while numeros:

    x = input('\n1,ingrese el numero\n2.No ingresar')
    if x == '1':
        y = float(input('\nIngrese el numero'))
        numerosAgregados.append(y)
    if x == '2':
        numeros = False




calculaMaxMin(numerosAgregados,mayorMenor)
print('El numero mayor es ',mayorMenor[0])
print('El numero menor es ',mayorMenor[1])
print(numerosAgregados)






