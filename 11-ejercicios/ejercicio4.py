"""
Ejercicio 4. 

Crear un script que tenga 4 variables:
- Lista
- String
- Entero
- Booleano

que imprima un mensaje segun el tipo de dato de cada variable. 
Usar funciones

"""
# crear funcion

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
        
    return result


def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    
    if test:
        result= f"Este dato es del tipo {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
        
    return  result
        

mi_lista = ["Hola", 98]
titulo = "Master Python"
numero = 22
falso = True

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(falso, bool))
