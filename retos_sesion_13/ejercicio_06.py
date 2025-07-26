while True:
    numero = int(input("Ingrese un número:  "))
    if numero ==0:
        break
    print("Multiplo de 7" if numero % 7 ==0 else "No es multiplo de 7")
