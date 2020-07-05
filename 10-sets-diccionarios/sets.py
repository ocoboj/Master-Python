"""
SET es un tipo de dato, para tener una colección de valores,
pero no tiene ni indice ni orden
"""

personas = {
    "Víctor",
    "Martin",
    "Pau"
}

personas.add("Olga")
personas.remove("Pau")

print(personas)
print(type(personas))