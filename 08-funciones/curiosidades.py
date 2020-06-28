"""
declarar funciones aquí arriba y es aconsejable poner return y no print
que será usado más abajo.
Acceder a variables globales pero que esten definidas antes de ejecutar la función
"""

def mi_funcion(nombre):
    return "Hola que tal " + nombre
    
def mi_segunda_funcion(apellidos):
    return "Hola que tal 2 " + apellidos
    
nombre = "Olga"
apellidos = "Conesa"

print("Hola Mundo")
print(f"Bienvenido {nombre}")

print (mi_funcion(nombre))
print (mi_segunda_funcion(apellidos))