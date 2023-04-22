import json
import os

ruta = './simulacro prueba/json/biblioteca.json'

biblioteca = {
    "bookstore": {
        "book": [
            {
                "title": {
                    "_lang": "en",
                    "__text": "Everyday Italian"
                },
                "author": "Giada De Laurentiis",
                "year": "2005",
                "price": "30.00",
                "_category": "COOKING"
            },
            {
                "title": {
                    "_lang": "en",
                    "__text": "Harry Potter"
                },
                "author": "J K. Rowling",
                "year": "2005",
                "price": "29.99",
                "_category": "CHILDREN"
            },
            {
                "title": {
                    "_lang": "en",
                    "__text": "XQuery Kick Start"
                },
                "author": [
                    "James McGovern",
                    "Per Bothner",
                    "Kurt Cagle",
                    "James Linn",
                    "Vaidyanathan Nagarajan"
                ],
                "year": "2003",
                "price": "49.99",
                "_category": "WEB"
            },
            {
                "title": {
                    "_lang": "en",
                    "__text": "Learning XML"
                },
                "author": "Erik T. Ray",
                "year": "2003",
                "price": "39.95",
                "_category": "WEB"
            }
        ]
    }
}

def crearJson(dato = biblioteca):
    with open(ruta, 'w') as archivo:
        json.dump(dato,archivo)
    archivo.close()

def leerJson():
    with open(ruta,'r') as archivo:
        biblioteca = json.load(archivo)
    archivo.close()
    return biblioteca

def menuGeneral():
    os.system('clear')
    menu = input('Seleccione\n1. Mostrar en pantalla todos los libros (titulo y autor (es))\n2. Crear mnuevo libro con la posiblidad de multiplies autores por libro\n3. Mostrar los datos de un libro consultado por el titulo\n4. Actualizar los datos de un libro consultado por el titulo\n5. Eliminar un libro de la biblioteca\n6. Salir\n')
    return menu

def mostrarBiblioteca(biblioteca,cantidad):
    os.system('clear')
    print('LIBROS\t\t\tAUTORES\n')
    for i in range(cantidad):
        libro = biblioteca["bookstore"]["book"][i]['title']['__text']
        if type(biblioteca["bookstore"]["book"][i]['author']) == str:
            autor = biblioteca["bookstore"]["book"][i]['author']
        else:
            autor = ''
            autores = biblioteca["bookstore"]["book"][i]['author']
            for i in autores:
                autor += i +','+ ' '

        print(libro,'\t\t',autor)

try:
    leerJson()
except FileNotFoundError:
    crearJson()

menu = menuGeneral()

while menu != '6':
    match menu:
        case '1':
            biblioteca =  leerJson()
            cantidad = len(biblioteca["bookstore"]["book"])
            print(cantidad)
            mostrarBiblioteca(biblioteca,cantidad)
            input('\nPresione enter para salir')
        case '2':
            os.system('clear')

            titulo = input('Ingrese el nombre del libro: ')
            idioma = input('Iingrese el lenguaje del libro: ')
            año = input('Ingrese el año: ')
            precio = input('Ingrese el precio: ')
            categoria = input('Ingrese la categoria: ')
            os.system('clear')
            numLibros = input('Su libro tinen varios autores\n1.No\n2.Si\n')

            if numLibros == '1':
                
                autor = input('Ingrese el autor ')
            elif numLibros == '2':
                autor = []
                numAutor = int(input('Ingrese el numero de autores '))
                for i in range(numAutor):
                    autores = input('\nIngrese el nombre del autor')
                    autor.append(autores)

            dicc = { "title": {"_lang": idioma, "__text": titulo}, "author": autor, "year": año, "price": precio, "_category": categoria }

            biblioteca["bookstore"]["book"].append(dicc)
            
            crearJson(biblioteca)
            
            input('\nSe añadio exitosamente presione enter para continuar')
        case '3':
            os.system('clear')
            biblioteca = leerJson()
            cantidad = len(biblioteca["bookstore"]["book"])

            mostrarBiblioteca(biblioteca,cantidad)

            libro = input('\nIngrese el nombre del libro ')
            cantidad = len(biblioteca["bookstore"]["book"])
            

            for i in range(cantidad):
                if libro == biblioteca["bookstore"]["book"][i]['title']['__text']:

                    idioma = biblioteca["bookstore"]["book"][i]['title']["_lang"]
                    nombre = biblioteca["bookstore"]["book"][i]['title']["__text"]
                    año = biblioteca["bookstore"]["book"][i]["year"]
                    precio = biblioteca["bookstore"]["book"][i]["price"]
                    categoria = biblioteca["bookstore"]["book"][i]["_category"]

                    if type(biblioteca["bookstore"]["book"][i]['author']) == str:
                        autor = biblioteca["bookstore"]["book"][i]["author"]
                    else:
                        autor = ''
                        autores = biblioteca["bookstore"]["book"][i]["author"]
                        for i in autores:
                            autor += i + ',' + ' '
                    os.system('clear')
                    print(' Nombre: ',nombre,'\n','Idioma: ',idioma,'\n','Autor o autores: ',autor,'\n','Año: ',año,'\n','Precio: ',precio,'\n','Categoria: ',categoria)
                    input('\nPresione cualquier letra para salir')
        case '4':
            os.system('clear')
            biblioteca = leerJson()
            cantidad = len(biblioteca["bookstore"]["book"])

            mostrarBiblioteca(biblioteca,cantidad)

            libro = input('\nIngrese el nombre del libro ')

            for i in range(cantidad):
                if libro == biblioteca["bookstore"]["book"][i]['title']['__text']:
                    os.system('clear')
                    biblioteca["bookstore"]["book"][i]['title']["_lang"] = input('Ingrese el lenguaje del libro: ')
                    biblioteca["bookstore"]["book"][i]['title']["__text"] = input('Ingrese el nombre del libro: ')
                    biblioteca["bookstore"]["book"][i]["year"] = input('Ingrese el año del libro: ')
                    precio = biblioteca["bookstore"]["book"][i]["price"] = input('Ingrese el precio del libro: ')
                    categoria = biblioteca["bookstore"]["book"][i]["_category"] = input('Ingrese la categoria del libro: ')

                    numAutor = input('\nSeleccione:\n1.Para un autor\n2.Varios autores\n')

                    if numAutor == '1':
                        biblioteca["bookstore"]["book"][i]["author"] = input('Ingrese el nombre del valor')
                    else:
                        autor = []
                        numAutor = int(input('\nIngrese el numero de autores '))
                        
                        for i in range(numAutor):
                            autores = input('\nIngrese el nombre del autor ')
                            autor.append(autores)

                        biblioteca["bookstore"]["book"][i]["author"] = autor

                    crearJson(biblioteca)
                    input('Editado exitosamente presione enter para continuar')
        case '5':
            biblioteca = leerJson()
            cantidad = len(biblioteca["bookstore"]["book"])
            mostrarBiblioteca(biblioteca,cantidad)
            j = 0

            libro = input('\nIngrese el nombre del libro ')

            for i in range(cantidad):
                if libro == biblioteca["bookstore"]["book"][i]['title']['__text']:
                    j = i
            biblioteca["bookstore"]["book"].pop(j)

            crearJson(biblioteca)

            input('Eliminado exitosamente presione enter para salir ')
        case other:
            print('Seleccion invalida')
    menu = menuGeneral()




                    


                            



            

            
        # {"title": {"_lang": "en", "__text": "Everyday Italian"}, "author": "Giada De Laurentiis", "year": "2005", "price": "30.00", "_category": "COOKING"}

