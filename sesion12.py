# print ("Inicio")
# condicion = True
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# print ("Fin")

# print ("Inicio")
# numero = 4
# if numero % 2 == 0: # Si el módulo de 2 es 0
#     print ("El número es par")
# print ("Fin")

# print ("Inicio")
# condicion = False
# if condicion:
#     # Bloque de código
#     print ("Cumple condición")
# else:
#     # Bloque de código
#     print ("No cumple condición")
# print ("Fin")

# print ("Inicio")
# numero = 3
# if numero % 2 == 0: # Si el módulo de 2 es 0
#     print ("El número es par")
# else:
#     print ("El número es impar")
# print ("Fin")

# print ("Inicio Par, Impar o Cero")
# numero = 0  
# if numero > 0 or numero < 0:
#     if numero % 2 == 0: # Si el módulo de 2 es 0
#         print ("El número es par")
#     else:
#         print ("El número es impar")
# else:
#     print ("El número es cero")
# print ("Fin")

# print ("Inicio Par, Impar o Cero")
# numero = 1/2  
# if numero != 0:
#     if numero % 2 == 0: # Si el módulo de 2 es 0
#         print ("El número es par")
#     else:
#         print ("El número es impar")
# else:
#     print ("El número es cero")
# print ("Fin")


# # como se declara un elif
# print ("Inicio ELIF")
# condicion_1 = False
# condicion_2 = True
# if condicion_1:
#     print ("Cumple condición 1")
# elif condicion_2:
#     print ("Cumple condición 2")
# else:
#     print ("No cumple condición 1 ni 2")
# print ("Fin")


# print ("Inicio Par, Impar o Cero")
# numero = 0  
# if numero != 0:
#     print ("El número es par")
# elif numero % 2 !=0:
#     print("el número es impar")
# else:
#     print ("El número es cero")
# print ("Fin")

# # operador ternario
# print ("Inicio Ternario")
# condicion = True
# resultado = "Cumple" if condicion else "No cumple"
# print (resultado)
# print ("Fin")


# print ("Inicio Ternario Par, Impar")
# numero = 3
# resultado = "El número es par" if numero % 2 == 0 else "El número es impar"
# print (resultado)
# print ("Fin")

# print ("Truthiness Enteros")
# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))
# print (dividendo,divisor)
# if divisor: #divisor != 0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")


# print ("Truthiness Enteros")
# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))
# print (dividendo,divisor)
# if divisor: #divisor != 0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")
# print ("Truthiness Flotantes")
# dividendo = float(input("Dividendo: "))
# divisor = float(input("Divisor: "))
# print (dividendo,divisor)
# if divisor: #divisor != 0.0
#     print (dividendo / divisor)
# else:
#     print ("No se puede dividir entre cero")
# print ("Fin")

#Tienes un dispositivo que mide la temperatura y si la temperatura es mayor a 30°C enciende un ventilador y si es menor a 20°C lo apaga
# temperatura = float(input())
# if temperatura>30:
#     print("enciende el ventilador")
# elif temperatura<20:
#     print("apaga el ventilador")
# else:
#     print("no pasa nada")
cesta = ['manzanas','platanos','mangos']
print(cesta)
if 'manzanas' in cesta:
    print(f"Hay{cesta.count('manzanas')}")
else:
    print(f"no hay ")