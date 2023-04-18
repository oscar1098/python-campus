import os
diccionarioDocentes ={}

diccionarioCategoria = {1:25000,2:30000,3:40000,4:45000,5:60000}

def calcularHonorarios(diccionarioDocentes,diccionarioCatego,j):
    os.system('clear')
    try:
        id = int(list(diccionarioDocentes.keys())[-1])+1
    except IndexError:
        id = 1

    cantidadDocentes = int(input('Ingrese la cantidad de docentes '))
    for i in range(cantidadDocentes):
        nombre = input('Ingrese el nombre del profesor ')
        cedula = input('Ingrese la cedula ')
        horas = int(input('Digite el numero de horas trabajas'))
        honorario = horas*diccionarioCatego[j]
        diccionarioDocentes[id] = {'nombre':nombre, 'cedula':cedula, 'horas':horas, 'honorarios': honorario,'categoria': j}
        id +=1

menu = input('Seleccione la categoria del docente\n1.Categoria 1\n2.Categoria 2\n3.Categoria 3\n4.Categoria 4\n5.Categoria 5\n6.Mostar honorarios\n7.Salir\n')

while menu != '7':
    match menu:
        case '1':
            calcularHonorarios(diccionarioDocentes,diccionarioCategoria,1)
        case '2':
            calcularHonorarios(diccionarioDocentes,diccionarioCategoria,2)
        case '3':
            calcularHonorarios(diccionarioDocentes,diccionarioCategoria,3)
        case '4':
            calcularHonorarios(diccionarioDocentes,diccionarioCategoria,4)
        case '5':
            calcularHonorarios(diccionarioDocentes,diccionarioCategoria,5)
        case '6':
            os.system('clear')
            acum = 0
            print('nombre\t\tcategoria\thoras\thonorarios')
            for i in diccionarioDocentes:
                print(diccionarioDocentes[i]['nombre'],'\t\t',diccionarioDocentes[i]['categoria'],'\t\t',diccionarioDocentes[i]['horas'],'\t\t',diccionarioDocentes[i]['honorarios'])
                acum += diccionarioDocentes[i]['honorarios']
            print('El total en honorarios es ',acum)
            input()
        case other:
            print('Seleccion invalida')
    os.system('clear')
    menu = input('Seleccione la categoria del docente\n1.Categoria 1\n2.Categoria 2\n3.Categoria 3\n4.Categoria 4\n5.Categoria 5\n6.Mostar honorarios\n7.Salir\n')
        
