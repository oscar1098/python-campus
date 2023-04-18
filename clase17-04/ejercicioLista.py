 #? Se desea realizar un programa en el cual se ingresen N letras del abecedario, las cuales se deben almacenar en una lista.Una vez creada una lista, se desea conocer e imprimir la cantidad de vacolaes que se repitan

lista = []

for i in range(11):
    letra = input('Ingrese una letra ').upper()
    lista.append(letra)

print('numero de letras a ',lista.count('A'))
print('numero de letras e ',lista.count('E'))
print('numero de letras i ',lista.count('I'))
print('numero de letras o ',lista.count('O'))
print('numero de letras u ',lista.count('U'))