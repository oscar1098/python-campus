'''
Se desea realizar un programa en el cual se ingrese un texto determinado, el cual se debe almacenar en una lista cada una de las letras de este. Una vez creada la lista, se desea conocer e imprimir la cantidad de 'a' la cantidad de 'e', la cantidad de 'i', la cantidad de 'o' y la cantidad de 'u' en el arreglo
'''

texto = input('Ingrese el texto ')
arreglo = []
conta=0
conte=0
conti=0
conto=0
contu=0

for i in texto:
    if i != ' ':
        arreglo.append(i)
    if i == 'a':
        conta += 1
    elif i == 'e':
        conte +=1
    elif i == 'i':
        conti +=1 
    elif i == 'o':
        conto +=1
    elif i == 'u':
        contu +=1

print(arreglo)
print('cantidad de a ', conta)
print('cantidad de e ', conte)
print('cantidad de i ', conti)
print('cantidad de o ', conto)
print('cantidad de u ', contu)
print('Cantidad de letras ', len(arreglo))
print('Cantidad de palabras' ,len(texto.split()))