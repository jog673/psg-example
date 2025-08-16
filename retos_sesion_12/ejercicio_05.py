nombre = input("Ingresar Nombre: ")
telefono = input("Ingresar el numero de telefono más codigo del país 'Ejemplo= formato +59167109691' : ")

nombre_formato = nombre.strip().title()
telefono_formato = telefono.strip()
contactos=[]

nombre_valido = bool(nombre.strip())
telefono_valido = False


if len(telefono_formato) == 12 and telefono_formato[0] == "+" :
    if telefono_formato[1:].isdigit():
         telefono_valido = True

print("\n------------------")
if nombre_valido and telefono_valido:
    print("Contacto guardado")
    contactos.append((nombre_formato, telefono_formato))

else:
    
     print("Datos incorrectos")

print(f"Nombre: {nombre_formato}")
print(f"Telefono: {telefono_formato}")
print(contactos)