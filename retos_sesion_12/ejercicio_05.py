nombre = input("Ingresar Nombre: ")
telefono = input("Ingresar el numero de telefono más codigo del país 'Ejemplo= formato +59167109691' : ")
nombre_formato = nombre.strip().title()
cantidad_numeros =len(telefono)
contactos=[]
if nombre and cantidad_numeros==12 :
    print("------------------")
    print("Contacto guardado")
    contactos.append((nombre.strip(), telefono))

else:
     print("------------------")
     print("Datos incorrectos")
print(f"Nombre: {nombre_formato}")
print(f"Telefono: {telefono}")
print(contactos)