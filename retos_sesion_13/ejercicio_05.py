n = 8
for fila in range(n):
    for columna in range(n):
        if(fila+columna)%2 == 0:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()