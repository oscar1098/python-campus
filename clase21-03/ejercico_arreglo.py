#Arreglos

cont = ''
personas = ['Juan','Maria','Lina','Jhon'] #Vector de una dimension (Matriz)
num = [[2,8,9,8],[5,8,7,5],[2,8,8,6]] #Matriz de dos dimensiones 2*3


for i in range(3):
    for j in range(4):
        cont += str(num[i][j])
    print(cont)
    cont = ''