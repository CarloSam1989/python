nombres = []
def agregar_nombre(lista):
    nombre = input("Ingrese Nombre a Agregar: ")
    lista.append(nombre)
    print("agregado exitosamente...:D")
def eliminar_nombre(lista):
    nombre = input("Ingresa el nombre a eliminar: ")
    if nombre in lista:
        lista.remove(nombre)
        print("eliminado exitosamente...;D")
    else:
        print("Nombre no encontrado!!!")
def VER_LISTA(lista):
    print("Nombres:")
    for nombre in lista:
        print(nombre)
opcion = 0
while opcion != 4:    
    print("=====MENU=====")
    print("1-Agrega")
    print("2-Ver Datos")
    print("3-Eliminar")
    print("4-Salir")
    print("==============")
    opcion = int(input("Ingrese Una Opcion: "))
    if opcion == 1:      
        agregar_nombre(nombres)
    elif opcion == 2:
        VER_LISTA(nombres)
    elif opcion == 3:    
        eliminar_nombre(nombres) 
    elif opcion == 4:
        print("Saliendo del Sistema...") 
    else:
        print("ERRO!! Opcion no Valida") 



    











