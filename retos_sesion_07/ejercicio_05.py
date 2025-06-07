#Escribir un programa que reciba una cadena y retorna verdadero o falso si es palindrome sin importar los espacios, mayuscualas o minusculas
variable=(input("Ingresar una cadena:   "))
variable_2= "".join(filter(str.isalnum,variable)).lower()

palindromo = (variable_2==variable_2[::-1])
print(palindromo)