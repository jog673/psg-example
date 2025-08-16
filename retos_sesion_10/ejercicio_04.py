#Jane y Jhon llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a un candy bar. 
# Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. 
# A continuación tienes los postres que han ido pidiendo en cada salida:
Jane = {'Lemon Pie', 'Brownie', 'Tarta de manzana', 'Helado de chocolate', 'Flan'}
Jhon = {'Carrot Cake', 'Croissant de chocolate', 'Lemon Pie', 'Tarta de manzana', 'Pudding'}
interseccion = Jane.intersection(Jhon)
a=len(Jane)
b=len(Jhon)
c= a + b
print("Postres en comun: ",interseccion)
b=len(interseccion)
compatibles = len(interseccion)> c*0.5
print("Son compatibles?: ",compatibles)
porcentaje = (len(interseccion)/c)*100
print("Porcentaje en %:",porcentaje)


