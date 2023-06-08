continuar = True
lista = []
while continuar:
    print("1) Ver los nombres de la lista")
    print("2) Agregar un nombre a la lista")
    print("3) Buscar nombres de la lista")
    print("4) Eliminar nombres de la lista")
    print("5) Eliminar toda la lista")
    print("6) Salir")

    opcion = input("opcion N: ")
    print("-------------------")
    if int(opcion) == 1:
        print(lista)
        print("-------------------")
    elif int(opcion) == 2:
        print("-------------------")
        nombre = input("INGRESE UN NOMBRE PARA AGREGAR: ")
        lista.append(nombre)
        print("NOMBRE AGREGADO CORRECTAMENTE")
        print("-------------------")
    elif int(opcion) == 3: 
        buscar = input("INGRESE EL NOMBRE A BUSCAR: ")
        for x in lista:
            if x == buscar:
                print(buscar, " SÍ ESTÁ EN LA LISTA")
                break
            else:
                print(buscar, "NO ESTÁ EN LA LISTA")
    elif int(opcion) == 4:
        eliminar = input("INGRESE EL NOMBRE A ELIMINAR: ")
        for x in lista:
            eli = True
            if x == eliminar:
                lista.remove(eliminar)
                print(nombre, "NOMBRE ELIMINADO CORRECTAMENTE")
                eli = False
                break
            elif eli == True:
                print(nombre, "ESE NOMBRE A ELIMINAR NO ESTÁ EN LA LISTA")
    elif int(opcion) == 5:  # eliminar toda la lista
        confirmar = input("¿ESTÁ SEGURO DE QUIERE TODA LA LISTA? (1: Si / 2: No): ")
        if "1" == confirmar.lower():
            lista.clear()
            print("LISTA ELIMINADA CORRECTAMENTE")
            break
        elif "2" == confirmar.lower():
            print("LISTA NO HA SIDO ELIMINADA")
        else:
            print("Respuesta no válida")
    elif int(opcion) == 6: 
        print("Saliendo del systema")
        salir = False
    else:
        print("Opcion no valido")