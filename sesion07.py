simple = 'Mi cadena permite comillas "dobles" en una sola línea'
doble  = "Mi cadena permite comillas 'simples' en una sola línea"
triple_simple = '''Mi cadena
permite contenido 
en varias líneas y comillas "dobles" '''
triple_doble = """Mi cadena
permite contenido 
en varias líneas y comillas 'simples' """
print (simple)
print (doble)
print (triple_simple)
print (triple_doble)

entero = str(1)
flotante = str(1E-3)
hexadecimal = str(0xA)
booleano = str (True)
print (entero)
print (flotante)
print (hexadecimal)
print (booleano)
print (type(entero))
print (type(flotante))
print (type(hexadecimal))
print (type(booleano))

print('El mensaje enviado fue: "Hello, I\'m a message"')
print('El mensaje enviado fue: "Hello, I\'m a message"')
print ("El mensaje enviado fue: \"Hello, I\'m a message\"")
print ('El mensaje enviado fue: \"Hello, I\'m a message\"')





mensaje = "Hola,\n\teste es un mensaje \vcon algunos caracteres \
especiales como \\ y tabulador."
print(mensaje)

#Metodo Input
#el texto introducido es de una sola línea y se inserta al programa cuando se realiza Enter al terminar de escribir

entrada = input("Ingrese un valor")
print (entrada)
print (type(entrada))

#convierte en un entero el dato de entrada
entero = int(input("Ingrese un valor"))
print (entrada)
print (type(entrada))

#convierte en un flotante el dato de entrada
flotante = float(input("Ingrese un valor"))
print (entrada)
print (type(entrada))

#convierte en un booleano el dato de entrada
booleano = bool(int(input("Ingrese un valor")))
print (entrada)
print (type(entrada))


print("Indexado positivo")
fruta = "banana"
print(fruta)
print(fruta[0])
print(fruta[5])
print(fruta[-6])
print(fruta[-2])

#nos sirve para sacer rebandas de la cadena
print ("Slicing")
ciudad =  "LaPaz-Bolivia"
print (ciudad)
print ("Slicing con índices positivos")
print (ciudad[0:6])
print (ciudad[0:6:2])
print ("Slicing con índices negativos")
print (ciudad[-10:-2])
print (ciudad[-10:-2:2])

print ("Slicing sin índice inicial y final")
print (ciudad[:6])
print (ciudad[6:])
print ("Slicing sin índice inicial ni final")
print (ciudad[:])
print (ciudad[::2])
print ("Slicing sin índice inicial y final")
print (ciudad[:6])
print (ciudad[6:])
print ("Slicing sin índice inicial ni final")
print (ciudad[:])
print (ciudad[::2])
print ("Slicing sin índice inicial y final")
print (ciudad[:6])
print (ciudad[6:])
print ("Slicing sin índice inicial ni final")
print (ciudad[:])
print (ciudad[::2])

print ("Slicing con paso negativo")
print (ciudad[10:4:-1])
print (ciudad[10::-2])


#repetición de cadenas
print("repetición de candenas")
cadena = "-#-"
repetida = cadena * 10
print (repetida)



print ("Longitud de una cadena")
cadena = "Hola Mundo :D"
longitud = len(cadena)
print (cadena)
print (longitud, type(longitud))

