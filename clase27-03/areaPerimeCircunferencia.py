'''
Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
'''

def calcularAreaPerimetroCircunferencia(radio,arreglo):
    area = 3.14*(radio**2)
    perimetro = 2*3.14*radio
    arreglo[0] = area
    arreglo[1] = perimetro
    return arreglo

areaPerimetro = [0.0,0.0]

radio = float(input('\nIngrese el radio\n'))

calcularAreaPerimetroCircunferencia(radio,areaPerimetro)

print('El area del circulo es: ', areaPerimetro[0])
print('El perimetro del circulo es: ', areaPerimetro[1])


