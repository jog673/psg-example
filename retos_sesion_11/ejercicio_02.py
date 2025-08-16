# Crea un diccionario de alimentos y que alimentos domésticos lo consumen
alimentos_consumidos = { 'carne':['gato','perro'], 'zanahoria':['conejo','oveja']}
print(alimentos_consumidos)
alimentos_consumidos.update(maiz=['gallinas','gansos','patos','cerdos'],heno = ['vaca','ovejas','cerdos'], trigo=['gallinas', 'pollos'], lechuga = ['conejos','cobayas','tortugas'])
print(alimentos_consumidos)
existe = 'trigo' in alimentos_consumidos
print(f"Existe la comida trigo en los alimentos? : {existe}")
trigo = alimentos_consumidos.pop('zanahoria')
print(alimentos_consumidos)

