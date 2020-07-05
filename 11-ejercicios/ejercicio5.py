"""
Ejercicio 5. 
Crear una lista con el contenido de esta tabla:
ACCION   AVENTURA               DEPORTES
GTA      ASSASINS               FIFA21
COD      CRASH                  PRO21   
PUGB     PRINCE OF PERSIA       MOTO GP 21

Mostrar esta información ordenada
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUGB"]
    },
     {
        "categoria": "AVENTURA",
        "juegos": ["ASSASINS", "CRASH", "PRINCE OF PERSIA"]
    },
      {
        "categoria": "DEPORTES",
        "juegos": ["FIFA21", "PRO21", "MOTO GP 21"]
    },
    
]

# Mostrar información ordenada

for categoria in tabla:
    print(f"---------- {categoria['categoria']} ----------")
    for juego in categoria['juegos']:
        print(juego)
