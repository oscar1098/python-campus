import io
'''
open => abrir el archivo: nombre y modo (lectura (r),escritura(w),agregar(a))
write => Escribir en el archivo
read => leer informacion del archivo (Total)
readlines => Leer la informacion del archivo por linea
'''

archivo_texto = open('nombres.txt','w')

nom = 'Sergio Medina\nLuisa ruiz\nMario Moreno'
archivo_texto.write(nom)

archivo_texto.close()