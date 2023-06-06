salir = True
listado = []
while salir:
    print("\n1) Ver la lista")
    print("2) Agregar un nombre a la lista")
    print("3) Buscar si un nombre está en la lista")
    print("4) Eliminar un nombre de la lista")
    print("5) Eliminar toda la lista")
    print("6) Salir")

    opcion = input("-->")
    if int(opcion) == 1:  # ver
        print(listado)
    elif int(opcion) == 2:  # agregar un nombre
        nombre = input("INGRESE UN NOMBRE: ")
        listado.append(nombre)
        print("NOMBRE AGREGADO CORRECTAMENTE")
    elif int(opcion) == 3:  # buscar
        buscar = input("INGRESE EL NOMBRE A BUSCAR: ")
        for x in listado:
            if x == buscar:
                print(buscar, " SÍ ESTÁ EN LA LISTA")
                break
            else:
                print("NO ESTÁ EN LA LISTA")
    elif int(opcion) == 4:  # eliminar 1
        eliminar = input("INGRESE EL NOMBRE A ELIMINAR: ")
        for x in listado:
            no = True
            if x == eliminar:
                listado.remove(eliminar)
                print("NOMBRE ELIMINADO CORRECTAMENTE")
                no = False
                break
            elif no == True:
                print("ESE NOMBRE A ELIMINAR NO ESTÁ EN LA LISTA")
    elif int(opcion) == 5:  # eliminar toda la lista
        SoN = input("¿ESTÁ SEGURO DE QUIERE TODA LA LISTA? (S/N): ")
        if "s" == SoN.lower():
            listado.clear()
            print("LISTA ELIMINADA CORRECTAMENTE")
            break
        elif "n" == SoN.lower():
            print("LISTA NO HA SIDO ELIMINADA")
        else:
            print("Respuesta no válida")
    elif int(opcion) == 6:  # salir
        print("BYE BYE")
        salir = False
    else:
        print("NO VÁLIDO")
