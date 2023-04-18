 #? Ordenar listas

lista=[0,5,4,3,7,2,1,9]

print(lista)

lista.sort()
print(lista)

lista.sort(reverse = True)
print(lista)

n = len(lista)

for i in range(n-1):
    for j in range(i+1,n):
        if lista[i] > lista[j]:
            t = lista[i]
            lista[i] = lista[j]
            lista[j] = t
print(lista)