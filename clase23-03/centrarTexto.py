'''
Ejercicio 1Permalink

Crea un procedimiento EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.
'''


def escribirCentrado(texto):
    print('{:>85}'.format(texto))


escribirCentrado('Escribir texto centrado')





