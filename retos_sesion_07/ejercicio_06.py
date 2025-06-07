#EJEMPLO 1 IDENTIFICA SI LA CADENAS ES UN NOMBRE DE VARIABLE VALIDO EN PYTHON
a="1variable"
print("1variable")
print(a.isidentifier())
#EJEMPLO 2 DIVIDE LA CADENA EN 3 PARTES(ANTES, DURANTE, DESPUES)
texto = "Varible>=3.1415"
print(texto.partition(">="))
#EJEMPLO 3 COMPRUEBA SI TODOS LOS CARACTERES SON ESPACIOS EN BLANCO
print ("".isspace())
print ("Hola".isspace())
#EJEMPLO 4 ELIMINA EL PREFIJO O SUFIJO
texto = "https://python.org"
print(texto.removeprefix("https://"))  # "python.org"
#EJEMPLO 5 SIMILAR A LOWERR PERO MUCHO MAS GENERAL PARA COMPARACION EN DISTINTO IDIOMA
texto1, texto2 = "straße", "STRASSE"
print(texto1.casefold() == texto2.casefold())  # True (en alemán, "ß" equivale a "ss")