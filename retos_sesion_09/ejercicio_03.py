#Crear una lista de personas con 10 nombres de personas
#Obtener una sub lista de 5 a 9 con saltos de 2 en 2
#Buscar si existe el nombre "José" en la lista original
#Ordenar la sub lista alfabéticamente a-z
#Ordenar la lista original alfabéticamente descendente z-a
lista= ['Luis', 'Ayanin', 'Gabriel', 'Limber', 'Lucas', 'Margarita', 'Franz', 'Eduardo', 'Ivett', 'José']
print(lista)
sub_lista = lista[5:10:2]
print(sub_lista)
busqueda = 'José'
buscar_jose = busqueda in lista
print("Existe el nombre Jose:?",busqueda in lista, lista.index(busqueda))
sub_lista.sort()
print(sub_lista)
sub_lista.sort(reverse=True)
print(sub_lista)
