"""
Hacer un programa que muestra los numeros impares entre
dos numeros que decida el usuario
"""

numero1 = int(input("Introduzca el primer numero: "))
numero2 = int(input("Introduzca el segundo numero: "))


if numero1 < numero2:
    
    for x in range(numero1, (numero2 + 1)):
        if x%2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")
    
else:
    print("El numero 1 debe ser mayor al 2")
    
    