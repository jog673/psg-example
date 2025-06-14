#Las notas de un estudiante durante un semestre son:
#10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100
#Genera una tupla con los resultados y calcula el promedio para saber si aprobó o no el semestre utiliza la función sum() y len()

#El promedio debe ser mayor o igual a 51 para aprobar

tupla_1 = (10,61,0,21,22,0,32,30,41,51,5,23,100)
longitud = len(tupla_1)
suma = sum(tupla_1)
promedio = suma/longitud
print(promedio>=51)
