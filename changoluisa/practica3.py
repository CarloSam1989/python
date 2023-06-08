"""listas = [ "sarango","brito","landin","gracia","tinoco"]
listas.insert(5, "changoluisa ")
listas.append("blacio")
listas.sort(reverse= True)
print(listas)
numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

listas =[ [ "siguenz",0],[ "bonilla",6],["landin",10 ],[ "tinoco",10]]
arreglo = list(filter(lambda listas: listas [ 1] == 10, listas))
print(arreglo)1
"""


estudiantes = []
def agregar_estudiante():
    while True:
        try:
            nombre = input("Ingrese el nombre del estudiante: ")
            estudiantes.append({"nombre": nombre, "nota": None})
            print("Estudiante agregado correctamente.")
            break
        except:
            print("Error al agregar estudiante. Intente nuevamente.")
def ingresar_nota():
    while True:
        try:
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = float(input("Ingrese la nota correspondiente: "))
            
            for estudiante in estudiantes:
                if estudiante["nombre"] == nombre:
                    estudiante["nota"] = nota
                    print("Nota ingresada correctamente.")
                    return      
            print("Estudiante no encontrado.")
            break
        except:
            print("Error al ingresar la nota. Intente nuevamente.")
def mostrar_estudiantes():
    print("Lista de estudiantes:")
    for estudiante in estudiantes:
        print("Nombre:", estudiante["nombre"], "Nota:", estudiante["nota"])
def eliminar_estudiante():
    while True:
        try:
            nombre = input("Ingrese el nombre del estudiante a eliminar: ")   
            for estudiante in estudiantes:
                if estudiante["nombre"] == nombre:
                    estudiantes.remove(estudiante)
                    print("Estudiante eliminado correctamente.")
                    return
            
            print("Estudiante no encontrado.")
            break
        except:
            print("Error al eliminar estudiante. Intente nuevamente.")
while True:
    print("\n----- Menú -----")
    print("1. Reguistrar estudiante")
    print("2. Ingresar nota")
    print("3. Mostrar estudiantes")
    print("4. Eliminar estudiante")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        ingresar_nota()
    elif opcion == "3":
        mostrar_estudiantes()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        print("¡Adios Baquero!")
        break
    else:
        print("Opción inválida , seleccione nuevamente.")
