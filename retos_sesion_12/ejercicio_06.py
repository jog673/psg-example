datos = input("Ingrese los datos(formato: numero1, numero2, operacion):   ").strip()
partes = datos.split(",")
if len(partes) == 3:
    n1 = partes[0].strip()
    n2 = partes[1].strip()
    operacion = partes[2].strip()
    if n1.isdigit() and n2.isdigit():
        n1 = int(n1)
        n2 = int(n2)

        if operacion =='+':
            resultado = n1 + n2
        elif operacion == "-":
            resultado = n1 - n2
        elif operacion == "*":
            resultado = n1*n2
        elif operacion == "/":
            if n2 !=0:
                resultado = n1/n2
            else:
                print("Error:Division por cero")
        else:
            print("Error:operacion no valida")
    else:
        print("Error: solo se permite numeros enteros positivos")
else:
    print("Error: formato incorrecto")
print(f"Operacion:{n1},{n2},{operacion}")
print("---------")
print(f"Resultado:{resultado}")
            





