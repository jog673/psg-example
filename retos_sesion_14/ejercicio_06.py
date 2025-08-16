#Crear una función que reciba una lista de números y devuelva una lista con los números pares y otra lista con los números impares
def separar_pares_impares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pares,impares = separar_pares_impares(numeros)

print("pares", pares)
print("impares", impares)