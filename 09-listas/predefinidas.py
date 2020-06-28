cantantes = ['JLO', 'Chayanne','Laura', 'Queen']
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar una lista
#print(numeros)
numeros.sort()
#print(numeros)

# Agregar elementos dentro de una lista
cantantes.append("Lola Indigo")
cantantes.insert(1, "Bisbal")
#print(cantantes)

# Eliminar elementos por posición
cantantes.pop(1)
#Eliminar por su nombre
cantantes.remove('Lola Indigo')
#print(cantantes)

# Dar la vuelta a la lista
#print(numeros)
numeros.reverse()
#print(numeros)

# Buscar dentro de una lista
print('Laura' in cantantes)

# Contar elementos
print(cantantes)
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Queen"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)