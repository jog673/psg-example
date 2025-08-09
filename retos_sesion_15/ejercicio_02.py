class FrutaIncorrecta(Exception):
    pass
canasta = []
frutas_permitidas = ['🍅', '🍇', '🍈', '🍉', '🍊', '🍌', '🍍', '🍑']
while True:
    try:
        fruta = input("Ingrese un fruta: ")
        if fruta == "salir":
            break
        
        if not fruta in frutas_permitidas:
            raise FrutaIncorrecta("La Fruta no es válida")
        
        canasta.append(fruta)
    except FrutaIncorrecta as e:
        print("🚫 Error:",e)
    except Exception as e:
        print("☠️ Error", e)
    else:
        print("🤝 Fruta agregada")
    finally:
        print("Canasta: ", canasta)