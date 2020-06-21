"""
Pedir dos numero al usuario y hacer todas las operaciones

"""

numero1 = int(input("Introduzca el primer numero: "))
numero2 = int(input("Introduzca el segundo numero: "))


print("#### CALCULADORA ####")

# SUMA
print(f"La suma de {numero1} + {numero2} = {numero1 + numero2}")
print("suma: " + str(numero1+numero2))

# RESTA
print(f"La resta de {numero1} - {numero2} = {numero1 - numero2}")

# MULTIPLICACION
print(f"La multiplicación de {numero1} x {numero2} = {numero1 * numero2}")

# DIVISION
print(f"La división de {numero1} / {numero2} = {numero1 / numero2}")