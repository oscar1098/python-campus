'''
Dada la siguiente información sobre las calificaciones de estudiantes de una institución educativa:
• Código
• Nombre
• Nota 1 (Peso de 30%)
• Nota 2 (Peso de 30%)
• Nota 3 (Peso de 40%)
El proceso se termina cuando el código que se ingrese sea 999.(Bandera)
Se pide calcular:

La nota definitiva de cada estudiante e indicar con un mensaje si aprobó o reprobó, utilizando funciones
Para aprobar, la nota deber ser mayor o igual a 3.0 y la información en su totalidad se debe almacenar
en listas
'''

bandera = True
estudiantes = []

while bandera:
    codigo = int(input('Ingresar codigo '))
    if codigo == 999:
        bandera = False
    else:
        nombre = input('Ingrese el nombre ')
        nota1= float(input('Ingrese la nota 1 '))*0.3
        nota2= float(input('Ingrese la nota 2 '))*0.3
        nota3= float(input('Ingrese la nota 3 '))*0.4
        notaDef = nota1 + nota2 + nota3
        estudiantes.append([codigo,nombre,nota1,nota2,nota3,notaDef])
        if notaDef >= 3.0:
            print('Su nota es: ',notaDef,' aprobado')
        else:
            print('Su nota es: ',notaDef,' reprobado')


print(estudiantes)













