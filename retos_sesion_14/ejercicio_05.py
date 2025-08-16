# Crear una función que reciba una cadena y devuelva la cantidad de vocales que tiene
def cantidad_vocales(cadena):
    cadena = cadena.lower()
    vocales = sum([1 for letra in cadena if letra in "aeiou"])
    return vocales
cadena = "eucalipto"
resultado = cantidad_vocales(cadena)

print(resultado)