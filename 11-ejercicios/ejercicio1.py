"""
Ejercicio 1. Hacer un programa que tenga una lista 
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

# Hacemos la lista

numeros = [25, 6, 100, 89, 97, 3, 15, 76]

# Recorremos la lista y la mostramos
print("\nListado Numeros")
print("--------------------")
for numero in numeros:
    print(numero)
    
# Hacer funcion que recorra listas de numeros y devuelva un string
def mostrarLista(lista):
    resultado = ""
    
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado

print(mostrarLista(numeros))

# Ordenar Lista
numeros.sort()
print("\nLista ordenada")
print("--------------------")
print(numeros)
print(mostrarLista(numeros))

# Mostrar la longitud
print("\nMostrar longitud")
print("--------------------")
print(len(numeros))

# Buscar elemento que el usuario pida por teclado
print("\nBuscar en la lista")
print("--------------------")

busqueda = int(input("Introduce el numero: "))

# comprobar si el dato es entero
comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introducido el {busqueda}")
    
print(f"### Buscar en la lista el número {busqueda} ###")

try:
    search = numeros.index(busqueda)
    print(f"El número buscado existe en la lista, es el indice: {search}")

except:
    print("El número no está en la lista")
    