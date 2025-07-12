# Crea un diccionario de alimentos y que alimentos domésticos lo consumen
alimentos_consumidos = { 'carne':['gato','perro'], 'zanahoria':['conejo','oveja']}
print(alimentos_consumidos)
alimentos_consumidos.update(maiz=['gallinas','ganzos','patos','cerdos'],heno = ['vaca','ovejas','cerdos'], trigo=['gallinas', 'pollos'], zanahoria = ['conejos','cobayas','tortugas'])
print(alimentos_consumidos)
existe = 'trigo' in alimentos_consumidos
print(f"Existe la comida trigo en los alimentos? : {existe}")
trigo = alimentos_consumidos.pop('trigo')
print(alimentos_consumidos)

