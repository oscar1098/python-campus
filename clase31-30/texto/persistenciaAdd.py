import io

archivo_texto = open('./json/nombres.txt','a')

nom = '\nPedro Perez'
texto = archivo_texto.write(nom)

archivo_texto.close()



