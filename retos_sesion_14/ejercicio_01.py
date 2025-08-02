# Crea una funcion que reciba una lista de calificaciones y devuelva el promedio de las mismas. Las calificaciones son: 50, 75, 80, 91, 70
def calcular_promedio(lista):
    return sum(lista)/len(lista)
calificaciones = [50,75,80,91,70]

print(calcular_promedio(calificaciones))