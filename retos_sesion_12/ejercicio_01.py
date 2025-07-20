#Crea un script que pida un número entero y verifique si es múltiplo de 5 usando operador ternario
variable = int(input("Ingrese un número entero: "))
resultado = "Es múltiplo de 5" if variable%5==0 else "No es múltiplo de 5"
print(resultado)
