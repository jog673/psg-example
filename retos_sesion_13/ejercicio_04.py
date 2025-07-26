while True:
    frase = input("Ingresar una frase:  ")
    frase = "".join(filter(str.isalnum,frase)).lower()
    palindromo = ((frase==frase[::-1]))
    print(f"La frase es palindromo: {palindromo}")
    if frase == 'salir':
        break
print("Fin")


