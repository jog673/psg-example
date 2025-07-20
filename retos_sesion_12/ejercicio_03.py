# Jhon colecciona autos a escala 1:64, tiene los siguientes autos
jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

if jhon.isdisjoint(jess):
    print("No hay elementos comunes")
else:
    interseccion = jhon.intersection(jess)
    print("Los autos en comun son:")
    print(interseccion)
    