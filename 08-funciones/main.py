"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a 
la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES
nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro) -> se puede llamar las veces que queramos

"""

# Ejemplo 1

print("####### EJEMPLO 1 #######")

# Definir funcion
def muestraNombres():
    print("Víctor")
    print("Paco")
    print("Juan")
    print("Aitor")
    print("Nestor")
    print("\n")
    
# Invocar función
muestraNombres()



# Ejemplo 2: parametros

print("####### EJEMPLO 2 #######")

""" def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    
    if edad >= 18:
        print("Eres mayor de edad")
    
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarTuNombre(nombre, edad) """

print("\n")

# Ejemplo 3

print("####### EJEMPLO 3 #######")

print("\n")

def tabla(numero):
    print(f"Tabla de mutiplicar del número: {numero}")
    
    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
        
    print("\n")
    
tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1
print("------------------------------------------------")
for numero_tabla in range (1, 11):
    tabla(numero_tabla)
    
# Ejemplo 4: Parametros Opcionales

print("####### EJEMPLO 4 #######")

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
  
    if dni != None:
        print(f"DNI: {dni}")
    
getEmpleado("Olga Conesa", 646464664)

# Ejemplo 5: Return o devolver datos

print("\n####### EJEMPLO 5 #######")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    
    return saludo

print(saludame("Olga"))


# Ejemplo 6

print("\n####### EJEMPLO 6 #######")

def calculadora(numero1, numero2, basicas = False):
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    
    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"   
    else:
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(56, 5, True))
    
# Ejemplo 7

print("\n####### EJEMPLO 7 #######")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}" 
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}" 
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Olga", "Conesa Boj"))

# Ejemplo 8: Funciones Lambda: funciones anónimas (definidas en una linea)

print("\n####### EJEMPLO 8 #######")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2034))