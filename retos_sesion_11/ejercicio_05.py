#Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies
arca = {"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}
#Añade al arca 3 especies más usando update
arca.update({'🐎':2,'🐷':2,'🐰':2})
print(arca)
# Toma lista de los animales en el arca iterando el diccionario
iterador = iter(arca.items())
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)
siguiente = next(iterador)
print(siguiente)

# existe en el arca la especie dragón?

existe = '🐲' in arca
print(f"Existe en el arca la especie 🐲 ? : {existe}")

#elimina la especie unicornio del arca

unicornio = arca.pop('🦄')
print(arca)

#Modifica el valor de la especie jirafa por 2

arca['🦒'] = 2
print(arca)

# Vacía el arca despues del diluvio
arca.clear()
print(arca)


