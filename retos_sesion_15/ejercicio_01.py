def operacion(numero1, numero2):
    suma = numero1 + numero2
    print(f"La suma es: {suma}")
    resta = numero1 - numero2
    print(f"La resta es : {resta}")
    multiplicacion= numero1*numero2
    print(f"La multiplicación es: {multiplicacion}")
    try:
         division = numero1/numero2
         print(f"La división es: {division}")
    except ZeroDivisionError:
         print("❌Error: No se puede dividir entre cero")
      

while True:
    try:
        numero1 = input("Ingresar el primer numero: ")
        if numero1.lower() == "salir":
            break
        num1 = float(numero1)

        numero2 = input("Ingresar el segundo numero:  ")
        if numero2.lower() == "salir":
            break
        num2 = float(numero2)

        operacion(num1, num2)
    except ValueError as e:
        print("☠️ Error",e)

    
    

