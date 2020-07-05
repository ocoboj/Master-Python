"""
Ejercicio 3. Crear un programa que compruebe si una variable
está vacia, y si está vacia, rellenarla con texto en minusculas y
mostrarlo en mayusculas.
"""

texto = ""

if len(texto.strip()) <= 0:
    
    # mostrar el texto
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
    
else:
    print("La variable tiene contenido {texto}")