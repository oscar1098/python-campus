def fac(n):

    f = 1

    for i in range(1,n+1):
        f *= i

    return f

n = int(input('Ingrese n '))
r  = int(input('Ingrese r '))

c = fac(n)/(fac(n-r)*fac(r))

print(c)









