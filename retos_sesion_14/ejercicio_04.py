# Crear una función anónima para obtener el valor absoluto de un número
valor_absoluto = lambda numero: numero if numero>0 else numero*(-1)
resultado = valor_absoluto(-500)
print(resultado)