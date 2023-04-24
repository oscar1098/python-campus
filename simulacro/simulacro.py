from tabulate import tabulate
import json
import os

ruta = './simulacro/json/biblioteca.json'

def leerJson():
    with open(ruta,'r') as archivo:
        biblioteca = json.load(archivo)
    archivo.close()

    return biblioteca

def escribirJson(biblioteca):
    with open(ruta,'w') as archivo:
        json.dump(biblioteca,archivo)
    archivo.close()

def limpiarPantalla():
    os.system('clear')

def menuGeneral():
    limpiarPantalla()
    menuGene =input('Seleccione:\n\n1.Ver libros\n2.Crear libro\n3.Ver informacion de un libro por el titulo\n4.Editar un libro\n5.Eliminar un libro\n6.Salir\n-')

    return menuGene

def titulosMenu(opcion):
    limpiarPantalla()
    print(f'--------------------------------{opcion}--------------------------------\n')

def validarAutores(libro):
    if type(libro["author"]) == str:
        autor = libro["author"]
    else:
        autor= ''
        for autores in libro["author"]:
            autor += autores + ','+' '

    return autor

def crearAutor():
    numAutores = int(input('\nIngrese el numero de autores: '))

    if numAutores == 1:
        autor = input('\nIngrese el nombre del autor: ')
    else:
        autor = []
        for i in range(numAutores):
            autores = input('\nIngrese el nombre del autor: ')
            autor.append(autores)
    return autor

def mostrarLibros(biblioteca):
    arregloLibro = biblioteca["bookstore"]["book"]
    arregloImprimir = []
    
    for libro in arregloLibro:
        titulo = libro["title"]["__text"]
        autor = validarAutores(libro)
        imprimir = [titulo,autor]
        arregloImprimir.append(imprimir)
        
    print(tabulate(arregloImprimir,headers=['TITULO','AUTOR']))

def menuEditar():
    limpiarPantalla()
    menuEdit = input('Seleccione:\n1.Editar nombre\n2.Editar lengueaje\n3.Editar año\n4.Editar precio\n5.Editar categoria\n6.Editar autores\n7.Salir\n-')

    return menuEdit

menuGene = menuGeneral()

while menuGene != '6':
    match menuGene:
        case '1':
            titulosMenu('LIBROS')
            biblioteca = leerJson()
            mostrarLibros(biblioteca)
            input('\nPresione enter para continuar')
        case '2':
            titulosMenu('CREAR LIBRO')
            
            titulo = input('Ingrese el nombre del libro: ')
            lenguaje = input('Ingrese el lenguaje del libro: ')
            año = input('Ingrese el año del libro: ')
            precio = int(input('Ingrese el precio del libro: '))
            categoria = input('Ingrese la categoria del libro: ')
            autor = crearAutor()
           
            diccLibro = {"title": {"_lang": lenguaje,"__text": titulo},"author": autor,"year": "2005","price": precio,"_category": categoria}
            
            biblioteca = leerJson()
            biblioteca["bookstore"]["book"].append(diccLibro)
            escribirJson(biblioteca)

            input('\nSe agrego correctamente precione enter para continuar')
        case '3':
            titulosMenu('INFORMACION POR TITULO')
            biblioteca = leerJson()
            mostrarLibros(biblioteca)
            arregloLibro = biblioteca["bookstore"]["book"]
            titulo = input('\n\nIngrese el nombre del titulo: ')
            arregloImprimir= []

            for libro in arregloLibro:
                if libro["title"]["__text"] == titulo:
                    titulosMenu('INFORMACION POR TITULO')
                    titulo = ['TITULO:',libro["title"]["__text"]]
                    arregloImprimir.append(titulo)
                    titulo = ['LENGUAJE:',libro["title"]["_lang"]]
                    arregloImprimir.append(titulo)
                    titulo = ['AUTOR O AUOTORES:',validarAutores(libro)]
                    arregloImprimir.append(titulo)
                    titulo = ['AÑO:',libro["year"]]
                    arregloImprimir.append(titulo)
                    titulo = ['PRECIO:',libro["price"]]
                    arregloImprimir.append(titulo)
                    titulo = ['ATEGORIA:',libro["_category"]]
                    arregloImprimir.append(titulo)
            print(tabulate(arregloImprimir))
            input('\nPresione enter para continuar')
        
        case '4':
            titulosMenu('EDITAR LIBRO')
            biblioteca = leerJson()
            mostrarLibros(biblioteca)
            nombreLibro = input('\nIngrese el nombre del libro: ')

            for libro in biblioteca["bookstore"]["book"]:
                if nombreLibro == libro["title"]["__text"]:
                    menuEdit =  menuEditar()
                    while menuEdit !='7':
                        match menuEdit:
                            case '1':
                                dato = input('\nIngrese el nombre del titulo ')
                                libro["title"]["__text"] = dato
                                escribirJson(biblioteca)
                                input('Se edito correctamente')
                            case '2':
                                dato = input('\nIngrese el lenguaje del titulo ')
                                libro["title"]["_lang"] = dato
                                escribirJson(biblioteca)
                                input('Se edito correctamente')
                            case '3':
                                dato = input('\nIngrese el año del titulo ')
                                libro["year"] = dato
                                escribirJson(biblioteca)
                                input('Se edito correctamente')
                            case '4':
                                dato = input('Ingrese el precio del titulo ')
                                libro["price"] = dato
                                escribirJson(biblioteca)
                                input('Se edito correctamente')
                            case '5':
                                dato = input('Ingrese la categoria del titulo ')
                                libro["_category"] = dato
                                escribirJson(biblioteca)
                                input('Se edito correctamente')
                            case '6':
                                dato = crearAutor()
                                libro["author"] = dato
                                escribirJson(biblioteca)
                                input('Se edito correctamente')
                            case other:
                                print('Seleccion invalida')
                        menuEdit =  menuEditar()
        case '5':
            titulosMenu('ELIMINAR')
            biblioteca = leerJson()
            mostrarLibros(biblioteca)
            libroEliminar = input('\nIngrese le nombre del libro que quiere eliminar: ')

            cantidadLibros = len(biblioteca["bookstore"]["book"])

            for i in range(cantidadLibros):
                if biblioteca["bookstore"]["book"][i]["title"]["__text"] == libroEliminar:
                    id = i
            
                    biblioteca["bookstore"]["book"].pop(id)
                    escribirJson(biblioteca)
                    input('\nSe elimino exitosamente, presone enter para contiuar')
    menuGene = menuGeneral()