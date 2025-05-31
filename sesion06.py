print("Tipos de datos booleanos")
print (True)
print (False)
# Operaciones aritméticas con booleanos
print (True + True)
print (True * True)
print (True * False)
print (False + False)
print (False * False)

print ("Números y booleanos")
print (10 + True)
print (10 + False)
print (10 * True)
print (10 * False)


print("declarar variables booleanas")
var_booleana = True
print(var_booleana)
print(type(var_booleana))

var_booleana = bool(0)
print( var_booleana)
print(type(var_booleana))

var_booleana = bool(15)
print(var_booleana)
print(type(var_booleana))






print ("Operadores de comparación")
print (10 == 10)
print (10 != 10)
print (10 < 10)
print (10 > 10)
print (10 <= 10)
print (10 >= 10)
print (10 is 10)
print (10 is not 10)

print ("Asignación de variables")
x = 10
mayor_que_cero = x > 0
print (mayor_que_cero)
diferente_de_10 = x != 10
print (diferente_de_10)


primera_nota=15
segunda_nota=20
tercera_nota=16

print((primera_nota+segunda_nota+tercera_nota)>50)


numero=15
print((numero % 3 ==0) and (numero % 5==0) and (numero % 2 !=0))

print("cortocircuito con operador and")
x = 1
y = 0
print (x>2 and (x/y) >2) #cortocircuito
#print (x>0 and (x/y) >0)