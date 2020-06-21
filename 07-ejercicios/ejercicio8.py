"""
Crear un programa que diga cuanto es el X por ciento de X numero
20% de 150 por ejemplo
"""

numero = int(input("Introduce el numero: "))
porcentaje = int(input(f"Que porcentaje quieres sacar de {numero}?: "))

operacion = (numero * (porcentaje / 100))

print(f"El {porcentaje}% de {numero} es: {operacion}")