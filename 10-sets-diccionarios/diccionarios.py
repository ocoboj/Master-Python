"""
Diccionario:
Un tipo de dato que alamacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

persona = {
    "nombre" : "Olga",
    "apellidos": "Conesa",
    "web": "udemy.com"
}

""" print(persona)
print(type(persona))
print(persona["nombre"]) """

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Olga',
        'email': 'olga@olga.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salavador@salvador.com'
    }
]

print(contactos)
contactos[0]['nombre'] = 'Olgui'
print(contactos[0]['nombre'])

print("\nListado de Contactos: ")
print("-------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-------------------------------------")