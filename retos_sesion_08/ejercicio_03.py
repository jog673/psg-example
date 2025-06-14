#Ingresa una pregunta por teclado y almacena el valor en una tupla
#Concatena las tupla
#('¿', ) + pregunta + ('?', )
#Imprime el resultado concatenado
#Repite la tupla concatenada 2 veces e imprime el nuevo resultado
variable_1=input("Ingresar una pregunta:  ")
tupla=(variable_1,)
tupla1=('¿',)
tupla2=('?',)
concatenar = tupla1 + tupla + tupla2
print(concatenar)
repetir=concatenar*2
print(repetir)
