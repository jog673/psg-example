#3 Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online.
tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]
conjunto_1 = set(tienda_fisica)
conjunto_2= set(tienda_online)
#a Quienes compraron en ambos canales
interseccion = conjunto_1.intersection(conjunto_2)
print(interseccion)
#b Quienes compraron solo en la tienda física
diferencia_1 = conjunto_1.difference(conjunto_2)
print(diferencia_1)
#c quienes compraron solo online
diferencia_2 = conjunto_2.difference(conjunto_1)
print(diferencia_2)
