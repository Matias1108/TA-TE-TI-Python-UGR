def vista_tabla(tabla):
    for fila in tabla:
        for i in range(0, len(fila)):
            if i == len(fila) - 1:  # chequeo de si i es el ultimo de la fila para asegurarnos de que imprime bien
                print(fila[i], end="\n")
            else:
                print(fila[i], end="  ")

def actualizacionTabla(tabla, posicion, jugador):
    if jugador:
        signo = 'X'
    else:
        signo = 'O'

    if posicion == 1:
        if tabla[4][0] == ' ':
            tabla[4][0] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    elif posicion == 2:
        if tabla[4][2] == ' ':
            tabla[4][2] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    elif posicion == 3:
        if tabla[4][4] == ' ':
            tabla[4][4] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    elif posicion == 4:
        if tabla[2][0] == ' ':
            tabla[2][0] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    elif posicion == 5:
        if tabla[2][2] == ' ':
            tabla[2][2] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    elif posicion == 6:
        if tabla[2][4] == ' ':
            tabla[2][4] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    elif posicion == 7:
        if tabla[0][0] == ' ':
            tabla[0][0] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    elif posicion == 8:
        if tabla[0][2] == ' ':
            tabla[0][2] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    elif posicion == 9:
        if tabla[0][4] == ' ':
            tabla[0][4] = signo
            return 0
        else:
            return 'Lugar ocupado!'
    else:
        return 'Lugar invalido!'

def combinaciones_posibles(tabla):
    for signo in ['X', 'O']:
        fila_0 = tabla[0][0] == signo and tabla[0][2] == signo and tabla[0][4] == signo
        fila_2 = tabla[2][0] == signo and tabla[2][2] == signo and tabla[2][4] == signo
        fila_4 = tabla[4][0] == signo and tabla[4][2] == signo and tabla[4][4] == signo
        columna_0 = tabla[0][0] == signo and tabla[2][0] == signo and tabla[4][0] == signo
        columna_2 = tabla[0][2] == signo and tabla[2][2] == signo and tabla[4][2] == signo
        columna_4 = tabla[0][4] == signo and tabla[2][4] == signo and tabla[4][4] == signo
        diagonal_1 = tabla[0][0] == signo and tabla[2][2] == signo and tabla[4][4] == signo
        diagonal_2 = tabla[0][4] == signo and tabla[2][2] == signo and tabla[4][0] == signo

        if fila_0 or fila_2 or fila_4 or columna_0 or columna_2 or columna_4 or diagonal_1 or diagonal_2:
            if signo == 'X':
                return 1
            elif signo == 'O':
                return 2

    return 0


tabla = [
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
]

vista_tabla(tabla)

primerTurno = True
jugador1 = ""
jugador2 = ""
turno = 0

while turno < 9:
    if jugador1 == '':
        print("Nombre jugador 1 (X)")
        jugador1 = input()
        print("Nombre jugador 2 (O)")
        jugador2 = input()
    else:
        if primerTurno:
            print(jugador1 + " es tu turno")
        else:
            print(jugador2 + " es tu turno")

        jugadaElegida = int(input())

        resultado = actualizacionTabla(tabla, jugadaElegida, primerTurno)
        while resultado != 0:
            print(resultado)
            jugadaElegida = int(input())
            resultado = actualizacionTabla(tabla, jugadaElegida, primerTurno)

        vista_tabla(tabla)
        ganador = combinaciones_posibles(tabla)
        if ganador == 1:
            print(jugador1 + ' es el ganador')
            break
        elif ganador == 2:
            print(jugador2 + ' es el ganador')
            break

        primerTurno = not primerTurno
        turno += 1

if turno == 9:
    print('Es un empate')
