# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores

""" try:

    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, pon bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteracción !!") """
    

# Multiples excepciones

""" try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado del numero es : "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código")
#except ValueError:
#   print("Introduce un numero correcto")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name_) """
    
# Excepciones personalizadas o lanzar excepeciones

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <=1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al master en python {nombre} !!")
except ValueError:
    print("Introduce los datos correctamente !")
except Exception as e:
    print("Existe un error: ", e)