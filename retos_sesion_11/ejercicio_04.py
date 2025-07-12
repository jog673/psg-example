# Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales en peligro de extinción con información sobre sus hábitats amenazados, lo que permite priorizar la protección de áreas críticas para la supervivencia de estas especies
habitats_peligro = {"polo norte":{"especies": {"oso polar","morsa","ballena"},"amenaza":{"contaminacion","cambio climatico"}},
                    "amazonas":{"especies":{"tigre", "mono", "guacamayo"},"amenaza":{"tala ilegal","deforestacion"}},
                    "atlantico":{"especies":{"vaca marina","tortuga","pinguino"},"amenaza":{"contaminacion marina","pesca ilegal"}},
                    "andes tropicales":{"especies":{"oso de anteojos", "puma andino"},"amenaza":{"mineria"}}
                    }

print(habitats_peligro)
habitats_peligro.update({"islas oceanicas":{"especies":{"pinguino galapagos","loro kakapo"},"amenaza":{"especies invasoras","perdida de habitat"}},
                         "asia":{"especies":{"tigre bengala","rinoceronte java"}, "amenaza":{"expansion agricola","urbanizacion"}}
                         })
print(habitats_peligro)
existe = "amazonas" in habitats_peligro
print(f"Existe en el diccionario habitat amazonas?: {existe}")
habitats_peligro['amazonas']['especies'].update({'anaconda'})
print(habitats_peligro)


