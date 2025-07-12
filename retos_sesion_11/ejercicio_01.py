#Utiliza un diccionario para almacenar información de un animal marino de un acuario, registra información como especie, habitat, dieta, estado de salud, edad y en un set los nombre de los responsables de su cuidado
animal_marino = {'Especie': 'Delphinidae', 
                 'Habitad':'Laguna', 
                 'Dieta':{ 'Peces':'Sardinas', 'Calamares':'Loligo',}, 
                 'Estado de salud':'Saludable', 
                 'Edad':'2', 
                 'Responsables':{'Jorge','Gabriel','Limber'}}
for clave, valor in animal_marino.items():
    print(f"{clave}:{valor}")

