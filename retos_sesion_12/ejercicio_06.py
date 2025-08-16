datos = input("Ingrese los datos(formato: numero1, numero2, operacion):   ").strip()

if datos.count(",") == 2:
    partes = [p.strip() for p in datos.split(",")]

    if partes[0] != "" and partes[1] != "" and partes[2] != "":
        n1_entrada, n2_entrada,operacion = partes
    
    
        if n1_entrada.isdigit() and n2_entrada.isdigit():
             n1 = int(n1_entrada)
             n2 = int(n2_entrada)

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
                  resultado = None
             else:
                print("Error:operacion no valida")
                resultado = None

             if resultado is not None:
               print(f"Operación:{n1_entrada},{n2_entrada},{operacion}")
               print(f"Resultado:{resultado}")
        else:
           print("Error: solo se permiten números enteros positivos")
    else:
        print("Error: formato incorrecto. No deje campos vacíos (ej.: 10, 5, +)")
else:
    print("Error: formato incorrecto. Use: numero1,numero2, operacion(ejemplo:10,5,+)")

            





