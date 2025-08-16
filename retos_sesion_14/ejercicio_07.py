tablero = [["" for i in range(3)] for j in range(3)]
turno = "X"
juego_terminado = False

def mostrar_tablero():
    print("\nTablero")
    for fila in tablero:
        print("|".join(fila))
        print("-"*9)

def verificar_victoria(jugador):
    for i in range(3):
        if tablero[i][0] == jugador and tablero[i][1] == and tablero[i][2] == jugador:
            return True