"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podem usar un indice númerico.
"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]

# Se puede crar una lista con la función list
cantantes = list(('2pac', 'Drake', "JLo"))

# crear una lista por rangos
years = list(range(2020, 2050))

# Crear lista variada de datos
variada = ["Olga", 39, 4.4, True, "Texto"]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# Indices

# Modificar un indice
pelicula = "otra cosa"
peliculas[1] = "Gran Torino"
peliculas[2] = "El Hobbit"
print(peliculas)

print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:2])
print(peliculas[1:]) # muestra todos los elementos a partir del 1

# Añadir elementos a una lista
cantantes.append("Chayenne")
cantantes.append("Melendi")
print(cantantes)

# Recorrer elementos de una lista


""" nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input("\n Introduce la nueva pelicula: ")
    
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula) """
    
print("\n*********** LISTADO PELICULAS ***********")
""" for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula} \n") """
    
# Listas Multidimensionales (listas dentro de listas)
print("\n********** LISTADO DE CONTACTOS **********")

contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Olga',
        'olga@olga.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)  
        else:
            print("Email: " + elemento)
             
    print("\n")

#print(contactos[1][1])

