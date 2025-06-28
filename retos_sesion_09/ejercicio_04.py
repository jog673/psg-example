#Una dulceria tiene 2 listas una con los productos y otra con los precios
productos = ['Refrescos','Pan', 'Bon Bon Bum','Oreo','Chizitos']
precios = [4, 0.5, 3, 2.5, 2]
# 1 Agregar 2 productos nuevos al final de las listas
print("\n")
print("1 Agregar 2 productos nuevos al final de las listas")
productos.append('Galletas')
productos.append('Chupete')
print (productos)

precios.append(1)
precios.append(0.8)
print (precios)

# 2 Eliminar el producto con el nombre "Bon Bon Bum"
print("\n")
print("2 Eliminar el producto con el nombre Bon Bon Bum")

productos.remove('Bon Bon Bum')
precios.remove(3)
print(productos)
print(precios)

# 3 Cuánto cuesta el producto "Oreo" y "Chizitos"
print("\n")
print("3 Cuánto cuesta el producto Oreo y Chizitos")
producto_buscado='Oreo'
indice= productos.index(producto_buscado)
print(producto_buscado,precios[indice])
producto_buscado2='Chizitos'
indice2=productos.index(producto_buscado2)
print(producto_buscado2,precios[indice2])

#4 Cual es el producto más caro y el más barato
print("\n")
print("4 Cual es el producto más caro y el más barato")


precio_caro=max(precios)
indice3 = precios.index(precio_caro)
print(precio_caro,productos[indice3])

precio_minimo=min(precios)
indice4 = precios.index(precio_minimo)
print(precio_minimo,productos[indice4])

# 5 cuantos productos tienes en total
print("\n")
print("5 cuantos productos tienes en total")
print(len(productos))

# 6 cuanto cuestan todos los productos
print("\n")
print("6 Cuanto cuestan todos los productos")
print(sum(precios))

# 7 Ordena los productos y precios del más barato al más caro
print("\n")
print("7 Ordena los productos y precios del más barato al más caro")
copia=precios[:]
copia.sort()
print(copia)
val_1=copia[0]
val_2=copia[1]
val_3=copia[2]
val_4=copia[3]
val_5=copia[4]
val_6=copia[5]

print(productos[precios.index(val_1)],productos[precios.index(val_2)],productos[precios.index(val_3)],productos[precios.index(val_4)],productos[precios.index(val_5)],productos[precios.index(val_6)])

#8 Eliminar todos los productos de las listas
print("\n")
print("8 Eliminar todos los productos de las listas")
print(productos)
print(precios)
productos.clear()
precios.clear()
print(productos)
print(precios)