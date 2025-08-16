while True:
    frase = input("Ingresar una frase:  ")
    if "salir" in frase.lower():
        break
    frase = "".join(filter(str.isalnum,frase)).lower()
    palindromo = ((frase==frase[::-1]))
    print(f"La frase es palindromo: {palindromo}")
print("Fin")


