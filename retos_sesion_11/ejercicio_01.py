#Utiliza un diccionario para almacenar información de un animal marino de un acuario, registra información como especie, habitat, dieta, estado de salud, edad y en un set los nombre de los responsables de su cuidado
animal_marino = {'Especie': 'Delphinidae', 
                 'Habitad':'Laguna', 
                 'Dieta':{ 'Peces':'Sardinas', 'Calamares':'Loligo',}, 
                 'Estado de salud':'Saludable', 
                 'Edad':'2', 
                 'Responsables':{'Jorge','Gabriel','Limber'}}
print("Especie:", animal_marino['Especie'])
print("Habitat:", animal_marino['Habitad'])
print("Dieta:", animal_marino['Dieta'])
print("Estado de salud:", animal_marino['Estado de salud'])
print("Edad:", animal_marino['Edad'])
print("Responsables:", animal_marino['Responsables'])

