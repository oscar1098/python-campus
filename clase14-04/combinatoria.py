n = int(input('Ingrese n '))
r = int(input('Ingrese r '))

fn = 1

for i in range(1,n+1):
    fn *= i

nr = n-r

fnr = 1

for i in range(1,nr+1):
    fnr *= i

fr = 1
    
for i in range(1,r+1):
    fr *=i

c = fn//(fnr*fr)

print(c)