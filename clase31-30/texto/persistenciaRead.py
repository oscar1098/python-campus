import io

archivo_texto = open('./json/nombres.txt','r')

texto = archivo_texto.read()

archivo_texto.close()

print(texto)

