"""
Ejercicio 3.

Escribir un programa que muestre los cuadrados
(numero mutiplicado por si mismo) de los 60 primeros numeros naturales.

    - resolver con for y while
"""

# WHILE
print("\n#### WHILE ####")


contador = 0

while contador <= 60:
    
    cuadrado = contador*contador
    
    print(f"El cuadrado de {contador} es {cuadrado}")
    
    contador +=1
    
# FOR

print("\n#### FOR ####")

for numero in range (61):
    
    cuadrado = numero*numero
    
    print(f"El cuadrado de {numero} es {cuadrado}")
      