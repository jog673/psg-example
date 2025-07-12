animales = (('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))
# Del diccionario obtén y elimina el valor de la clave 'aves'
animales_diccionario = dict(animales)
print(animales_diccionario)
aves = animales_diccionario.pop('aves')
print(animales_diccionario)
# Modifica el valor de la clave 'felino' por '🐈'
animales_diccionario['felino'] = '🐈'
print(animales_diccionario)
# Cambia la clave canino por canino y su valor por ['🐶','🐕']
animales_diccionario['caninos'] = ['🐶', '🐕']
del animales_diccionario['canino']
print(animales_diccionario)
