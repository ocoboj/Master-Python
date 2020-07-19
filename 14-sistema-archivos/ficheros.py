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