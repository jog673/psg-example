#Crear una función que reciba dos números y una operación (suma, resta, multiplicación, división) y devuelva el resultado de la operación
def operacion(numero1, numero2, operacion):
    if operacion == "+":
        return numero1 + numero2
    elif operacion == "-":
        return numero1 - numero2
    elif operacion == "*":
        return numero1*numero2
    elif operacion == "/":
        return numero1/numero2
    else:
        return "Operación no válida"
resultado = operacion(10,5,"+")
print(resultado)