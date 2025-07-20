# Tienes una app para gestionar tareas de 4 usuarios, para acceder los usuarios deben iniciar sesion con un nombre de usuario y una
#contraseña introducidos por teclado.
#Define los siguientes usuarios y contraseñas utilizando la estructura de datos más adecuada
licencias = {
    'admin': 'admin123',
    'user1': 'user123',
    'user2': 'user123',
    'user3': 'user123'
}

usuario = input("Escriba su usuario: ")
contraseña = input("Escriba su contraseña: ")

resultado='Acceso Aprobado' if usuario in licencias and licencias[usuario]==contraseña else 'Acceso denegado'
print(resultado)
