
"""
# Condicional if 

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

    if condicion:
        instrucciones
    else:
        otras instrucciones


# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores lógicos
and Y
or O
! negación
not No

"""

# Ejemplo 1
print("########## EJEMPLO 1 ########## ")

# queremos conseguir si el valor de la variable es rojo mostraremos un texto que el color es rojo sino no es rojo
color = "verde" 

# Haremos que el usuario introduzca el color

""" color = input("Adivina cual es mi color favorito: ") """

if color == "rojo" :
    print("Enhorabuena!!!")
    print("El color es ROJO")
else:
    print(f"El color NO es ROJO")
    
# Ejemplo 2
print("\n########## EJEMPLO 2 ########## ")

year = 2020
#year = int(input("en que año estamos: "))

# vamos a comprobar si el valor de year es mayor o igual que 2021

if year < 2021 :
    print("Estamos antes de 2021 !!")
else:
    print("Es un año posterior a 2021")

# Ejemplo 3
print("\n########## EJEMPLO 3 ########## ")

nombre = "Olga Conesa"
ciudad = "Vilanova"
continente = "Oceania"
edad = 39
mayoria_edad = 18

if edad >= mayoria_edad :
    print(f'{nombre} es mayor de edad !!')

    if continente != "Europa" :
        print ("El usuario NO es europeo ")
    else:
        print(f"Es Europeo y de {ciudad}")

else:
    print(f"{nombre} NO es mayor de edad")

    
# Ejemplo 4
print("\n########## EJEMPLO 4 ########## ")

""" dia = int(input("Introduce el numero de la semana: ")) """
dia = 2

"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")
"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana !!")
    
# Ejemplo 5
print("\n########## EJEMPLO 5 ########## ")

edad_minima = 18
edad_maxima = 65
edad_oficial = 25
""" edad_oficial = int(input("¿Tienes edad de trabjar? Introduce tu edad: ")) """

if edad_oficial >=18 and edad_oficial <= 65:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")
    
# Ejemplo 6
print("\n########## EJEMPLO 6 ########## ")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana !!")
else:
    print(f"{pais} no es de habla hispana")
    
# Ejemplo 7
print("\n########## EJEMPLO 7 ########## ")

pais = "USA"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana !!")
else:
    print(f"{pais} SI es de habla hispana")
    
# Ejemplo 8
print("\n########## EJEMPLO 8 ########## ")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana !!")
else:
    print(f"{pais} SI es de habla hispana")