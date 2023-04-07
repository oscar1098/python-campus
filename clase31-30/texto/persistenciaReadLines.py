import io

archivo_texto = open('./json/nombres.txt','r')

lista_nombres = archivo_texto.readlines()

archivo_texto.close()

print(lista_nombres)

for i in lista_nombres:
    print('nombre: ', i)
