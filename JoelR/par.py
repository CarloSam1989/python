opcion = True
while opcion:
    try:
        numero = int(input("Ingrese un número: "))
        if numero < 0:
            print("Ingrese un número válido.")
            continue

        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")

        pre = input("¿Desea salir del programa? (y/n): ")
        if pre == "y":
            opcion = False
        elif pre == "n":
            opcion = True
        else:
            print("Opción inválida. Saliendo del programa.")
            opcion = False

    except ValueError:
        print("Error: Ingrese solo números enteros.")
