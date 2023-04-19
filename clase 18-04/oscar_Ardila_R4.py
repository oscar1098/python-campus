from datetime import date
import os

pacientes = {}
def menuGeneral():
    os.system('clear')
    print('Seleccione\n1.Crear nuevo paciente\n2.Editar datos de un paciente\n3.Borrar datos de un paciente\n4.Listar todos los pacientes\n5.Salir')
    menu = input()
    return menu

def generarId(diccionario):
    try:
        id = int(list(diccionario.keys())[-1]) +1
        return id
    except IndexError:
        return 1
    
def mostrarPacientes(pacientes):
    os.system('clear')
    print('CODIGO\t\tNOMBRE\t\tFECHA NACIMIENTO\t\tPESO\t\tSEXO')
    for paciente in pacientes:
        print(paciente,'\t\t',pacientes[paciente]['nombre'],'\t\t',pacientes[paciente]['fecha'],'\t\t',pacientes[paciente]['peso'],'\t\t',pacientes[paciente]['sexo'])

def menuEditar():
    os.system('clear')
    print('Seleccione\n1.Editar nombre\n2.Editar Fecha de nacimiento\n3.Editar peso\n4.Editar sexo\n5.Salir')
    menuEditar = input()
    return menuEditar

def editar(llave,diccionario):
    os.system('clear')
    mostrarPacientes(diccionario)
    id = int(input('Ingrese el id '))
    print('Ingrese el nuevo',llave)
    dato = input()
    diccionario[id][llave] = dato

menu = menuGeneral()

while menu != '5':
    match menu:
        case '1':
            os.system('clear')
            id = generarId(pacientes)
            nombre = input('Ingrese el nombre del paciente ')
            fecha = input('Ingrese la fecha de nacimiento (dd/mm/aa) ')
            peso = input('Ingrese el peso del paciente ')
            sexo = input('Ingrese el sexo del paciente (Hombre/Mujer) ')
            pacientes[id]={'nombre':nombre,'fecha':fecha,'peso':peso,'sexo':sexo}
        case '2':
            menuEdit = menuEditar()
            while menuEdit != '5':
                match menuEdit:
                    case '1':
                        editar('nombre',pacientes)
                    case '2':
                        editar('fecha',pacientes)
                    case '3':
                        editar('peso',pacientes)
                    case '4':
                        editar('sexo',pacientes)
                    case other:
                        print('Seleccion invalida ')
                menuEdit = menuEditar()
        case '3':
            mostrarPacientes(pacientes)
            id = input('Ingrese el paciente que desea eliminar ')
            del(pacientes[id])
            input('Eliminacion exitosa precione cualquier letra para salir ')
        case '4':
            mostrarPacientes(pacientes)
            input()
        case other:
            print('Seleccion invalida')
    menu = menuGeneral()