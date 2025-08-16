# Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales en peligro de extinción con información sobre sus hábitats amenazados, lo que permite priorizar la protección de áreas críticas para la supervivencia de estas especies
habitats_peligro = {"polo norte":{"especies": {"oso polar","morsa","ballena"}},
                    "amazonas":{"especies":{"tigre", "mono", "guacamayo"},},
                    "atlantico":{"especies":{"vaca marina","tortuga","pinguino"}},
                    "andes tropicales":{"especies":{"oso de anteojos", "puma andino"}}
                    }

print(habitats_peligro)
habitats_peligro.update({"islas oceanicas":{"especies":{"pinguino galapagos","loro kakapo"}},
                         "asia":{"especies":{"tigre bengala","rinoceronte"}}
                         })
print(habitats_peligro)
existe = "amazonas" in habitats_peligro
print(f"Existe en el diccionario habitat amazonas?: {existe}")
habitats_peligro['amazonas']['especies'].update({'anaconda'})
print(habitats_peligro)


