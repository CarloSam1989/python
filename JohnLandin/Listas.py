listas = ["sarango", " blacio", "rojas", "landin", "garcia", "tinoco"]
# el metodo insert sirve para ingresar en cualquier posicion que se indique
listas.insert(2, "Changoluisa")
# el metodo append sirve para ingresar solamente al final de la lista
listas.append("Blacio")
# el metodo remove sirve para remover el nombre, y solo reconoce strings
listas.remove("Brito")
# el metodo pop elimina por numero de posicion ejm. 0 1 2 3 etc.
listas.pop(1)
# el metodo del elimina a segun el nuemro tambien pero con funciones de python
del listas[0]
# el metodo clear vacia compleramente la lista
listas.clear()
print(listas)
# el metodo sort ordena alfabeticamente, el arreglo reverse, hace que se ordenen al reves.
listas.sort(reverse=true)
# el metodo sorted hace lo mismo que el sort pero debe ser almacenado en una variable
arreglo = sorted(listas)
# este comando sirve para buscar en listas de listas
listas = [["siguenza", 0], ("bonilla", 0), ("landin", 10), ("tinoco", 10)]
arreglo = list(filter(lambda listas: listas[1] == 7, listas))
listas = ["siguenza", "Bonilla", "landin", "Tinoco"]
# este metodo try - except ValueError sirve para que cuando aparezca un error inesperado el programa siga su fincioanmiento y no se interrumpa
try:
    id = listas.index("garcia")
    print(id)
except ValueError:
    print("no hay")
