
arreglo = []
op = True
acum = ''
cont = 0

while op:
    estudiante = input('Ingrese el estudiante ')
    n1 = int(input('Ingrese la nota 1 '))
    n2 = int(input('Ibgrese la nota 2 '))
    n3 = int(input('Ibgrese la nota 3 '))
    nf = (n1+n2+n3)/3
    arreglo.append(estudiante)
    arreglo.append(n1)
    arreglo.append(n2)
    arreglo.append(n3)
    arreglo.append(nf)
    acum += str(arreglo[cont])+'\t\t'+str(arreglo[cont+1])+'\t'+str(arreglo[cont+2])+'\t'+str(arreglo[cont+3])+'\t'+str(arreglo[cont+4])+'\n'
    x = input('Agregar nuevo estudiante s/n ')
    if x == 'n':
        op = False
        print('\nEstudiante\tn1\tn2\tn3\tnf')
        print(acum)
    cont +=5
    
print(arreglo)
    
    


