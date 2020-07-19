from io import open
import pathlib 

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
""" print(ruta) """
""" archivo = open("14-sistema-archivos/fichero_texto.txt", "a+") """
archivo = open(ruta, "a+")

# Escribir
archivo.write("******* Soy un texto metido desde python *******\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
""" contenido = archivo_lectura.read()
print(contenido) """

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for frase in lista:
    """ lista_frase = frase.split()
    print(lista_frase) """
    if not frase.isnumeric():
        print(frase.center(100))