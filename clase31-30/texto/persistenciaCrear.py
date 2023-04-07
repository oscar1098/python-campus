import io
#Fase de creacion
archivo_texto = open("./json/nombres.txt","w")

#Fase de manipulacion
nom = 'Sergio Medina \nLuisa Ruiz \nMario Moreno'
archivo_texto.write(nom)

#Fase de cierre
archivo_texto.close()