puntos = ['Love',15,30,40]
p1 = 0
p2 = 0
op = True

print('\nSeleccione quien anoto punto\n1.Para jugador 1\n2.Para jugador 2')
m = int(input(':)_'))
if m == 1:
    p1 +=1
    print('\nJugador 1 tiene ',puntos[p1])
    print('Jugador 2 tiene ',puntos[p2])
elif m == 2:
    p2 +=1
    print('\nJugador 1 tiene ',puntos[p1])
    print('Jugador 2 tiene ',puntos[p2])

while op:
    if p1 == 3 and p2 == 0:
        print('\nJugador 1 gana')
        op = False
        
    elif p1 == 0 and p2 == 3:
        print('\nJugador 2 gana')
        op = False

    elif (p1 == 3 and p2 == 2) or (p1 == 3 and p2 == 1):
        print('\nSeleccione quien anoto punto\n1.Para jugador 1\n2.Para jugador 2')
        m = int(input(':)_'))
        if m == 1:
            print('\nJugador 1 gana')
            op = False
        elif m == 2:
            p2 +=1
            print('\nJugador 1 tiene ',puntos[p1])
            print('Jugador 2 tiene ',puntos[p2])

    elif (p1 == 2 and p2 == 3) or (p1 == 1 and p2 == 3):
        print('\nSeleccione quien anoto punto\n1.Para jugador 1\n2.Para jugador 2')
        m = int(input(':)_'))
        if m == 2:
            print('\nJugador 2 gana')
            op = False
        elif m == 1:
            p1 +=1
            print('\nJugador 1 tiene ',puntos[p1])
            print('Jugador 2 tiene ',puntos[p2])
    
    elif p1 == 3 and p2 == 3:
        p1 = 0
        p2 = 0
        empate = True
        while empate:
            if p1 == 0 and p2 == 0:
                print('\nDeuce')
                print('\nSeleccione quien anoto punto\n1.Para jugador 1\n2.Para jugador 2')
                m = int(input(':)_'))
                if m == 1:
                    p1 +=1
                    print('\nAd-in')
                    print('\nSeleccione quien anoto punto\n1.Para jugador 1\n2.Para jugador 2')
                    m = int(input(':)_'))
                    if m == 1:
                        print('\nAd-Out\nJugador 1 gana')
                        empate = False
                        op = False
                    if m == 2:
                        p1 -=1
                elif m == 2:
                    p2 +=1
                    print('\nAd-in')
                    print('\nSeleccione quien anoto punto\n1.Para jugador 1\n2.Para jugador 2')
                    m = int(input(':)_'))
                    if m == 2:
                        print('\nAd-Out\nJugador 2 gana')
                        empate = False
                        op = False
                    if m == 1:
                        p2 -=1
    else:
        print('\nSeleccione quien anoto punto\n1.Para jugador 1\n2.Para jugador 2')
        m = int(input(':)_'))
        if m == 1:
            p1 +=1
            print('\nJugador 1 tiene ',puntos[p1])
            print('Jugador 2 tiene ',puntos[p2])
        elif m == 2:
            p2 +=1
            print('\nJugador 1 tiene ',puntos[p1])
            print('Jugador 2 tiene ',puntos[p2])
                
                    


        

    
        