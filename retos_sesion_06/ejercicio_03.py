#Imprime una tabla de verdad para la siguiente sentencia: "Un sistema de seguridad controla el acceso a una habitación
# la puerta sólo se abre si se introduce una tarjeta válida o la huella dactilar, pero no ambas al mismo tiempo.
#Si se introduce la tarjeta y la huella dactilar, la puerta no se abre. ¿Qué operador lógico se puede utilizar?
tarjeta_valida=True
huella_dactilar=True
print((tarjeta_valida or huella_dactilar) and not (tarjeta_valida and huella_dactilar))
tarjeta_valida=True
huella_dactilar=False
print((tarjeta_valida or huella_dactilar) and not (tarjeta_valida and huella_dactilar))
tarjeta_valida=False
huella_dactilar=True
print((tarjeta_valida or huella_dactilar) and not (tarjeta_valida and huella_dactilar))
tarjeta_valida=False
huella_dactilar=False
print((tarjeta_valida or huella_dactilar) and not (tarjeta_valida and huella_dactilar))
