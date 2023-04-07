'''
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
'''

arreglo = [0.0,False]
usuario = ''
contraseña = ''

def login(usuario,contraseña,arreglo):
    intentos = True
    contador = 0
    while intentos:
        usuario = input('\nIngrese el usuario ')
        contraseña = input('\nIngrese la contraseña ')
        if usuario != 'usuario1' and contraseña !='asdasd':
            contador += 1
            arreglo[0] = contador
        else:
            intentos = False
            arreglo[1] = True
            return arreglo, contador
        
login(usuario,contraseña,arreglo)
print('\n',arreglo[1])
print('\nIntento entrar ',arreglo[0],' veces')

for i in range(3):
    usuario = input('Ingrese el usuario ')
    contraseña = input('Ingrese la contraseña ')
    if usuario == 'usuario1' and contraseña == 'asdasd':
        print(True)
        break
    elif i == 2:
        print(False)







