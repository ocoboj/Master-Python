from io import open
import pathlib 
import shutil

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
        
# Copiar archivo
"""
ruta_original= str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa =  str(pathlib.Path().absolute()) + "/07-ejercicios/fichero_copiado88.txt"

shutil.copyfile(ruta_original, ruta_alternativa)
"""
# Mover archivo o renombrarlo
""" ruta_original= str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva) """

# Eliminar archivos
""" import os

ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

os.remove(ruta_nueva) """

# Comprobar si un archivo existe
import os.path

""" print(os.path.abspath("../")) """
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")