# Para crear variables no se pueden poner caracteres como tíldes, palabras reservadas...

mi_texto = "Hola"
miTexto = "Mundo"

texto_unido = mi_texto + " " + miTexto

print(texto_unido)

# Mostrar uno de los textos entre ""

mi_texto = '"Hola"'
miTexto = " \"Mundo\""

texto_unido = mi_texto + " " + miTexto

print(texto_unido)

# Uso de valores especiales para que se interpreten cuando inicias el programa

# Salto de línea
texto_unido = mi_texto + " \n" + miTexto
print(texto_unido)

# Tabulación
texto_unido = mi_texto + " \t " + miTexto
print(texto_unido)

# Borra la primera variable
texto_unido = mi_texto + " \r " + miTexto
print(texto_unido)