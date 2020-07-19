"""
Modulos: son funcionalidades ya hechas para reutilizar.
"""
# Importar modulo propio
""" import mimodulo """
# Si quiero importar solo una función
""" from mimodulo import holaMundo """
# Si quiero importar todas las funciones
from mimodulo import *

""" print(mimodulo.holaMundo("Olga Conesa"))
print(mimodulo.calculadora(3,5,True)) """

# Para llamar a la función desde el import
print(holaMundo("Olga Conesa"))
print(calculadora(3,5,True))

