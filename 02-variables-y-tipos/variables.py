"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto 
"""

# Crear variables y asignarels un valor
texto = "Máster en Python"
numero = 45
decimal = 6.7

# Mostrar las variables
print(texto)
print(numero)
print(decimal)

print("-------------------------------------")

# Sustituir el valor de algunas variables / reasignado valores

numero = 77
decimal = 8.9

print(numero)
print(decimal)

print("-------------------------------------")

# Concatenación
nombre = "Olga"
apellidos = "Conesa Boj"
web = "https://www.udemy.com"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y la web del master es: {}".format(nombre, apellidos, web))