def suma():
    total_datos = int(input("Ingresa el total de datos a sumar: "))
    suma = float(input("Ingrese el primer dato: "))
    for i in range(1, total_datos):
        dato = float(input(f"Ingrese el dato #{i + 1}: "))
        suma = suma + dato
    return suma

def resta():
    total_datos = int(input("Ingresa el total de datos a restar: "))
    resta = float(input("Ingrese el primer dato: "))
    for i in range(1, total_datos):
        dato = float(input(f"Ingrese el dato #{i + 1}: "))
        resta = resta - dato
    return resta

def multiplicacion():
    total_datos = int(input("Ingresa el total de datos a multiplicar: "))
    producto = float(input("Ingrese el primer dato: "))
    for i in range(1, total_datos):
        dato = float(input(f"Ingrese el dato #{i + 1}: "))
        producto = producto * dato
    return producto

def division():
    total_datos = int(input("Ingresa el total de datos a dividir: "))
    resultado = float(input("Ingrese el primer dato: "))
    for i in range(1, total_datos):
        dato = float(input(f"Ingrese el dato #{i + 1}: "))
        if dato != 0:
            resultado = resultado / dato
        else:
            print("Error: No se puede dividir entre cero.")
            return None
    return resultado


menu = 0
while menu != 5: 
    print("------------Menu-------------")
    print("| 1° Sumar                  |")
    print("| 2° Restar                 |")
    print("| 3° Multiplicar            |")
    print("| 4° Dividir                |")
    print("| 5° Salir                  |")
    print("-----------------------------")
    menu = int(input("Ingrese una Opcion: "))
    print("-----------------------------")
    if menu == 1:
        print("| Suma                      |")
        resultado = suma()
        print("| La suma de los datos es:", resultado)
        print("-----------------------------")
    elif menu ==2:
        print("| Resta                     |")
        resultado = resta()
        print("| La resta de los datos es:", resultado)
        print("-----------------------------")
    elif menu ==3:
        print("| Multiplicar               |")
        resultado_multiplicacion = multiplicacion()
        print("| La multiplicacion de los datos es:",resultado_multiplicacion)
        print("-----------------------------")
    elif menu ==4:
        print("| Dividir                   |")
        resultado_division = division()
        if resultado_division is not None:
            print("| La resta de los datos es:",resultado_division)
            print("-----------------------------")
    elif menu ==5:
        print("| Saliendo del Sistema...   |")
        print("-----------------------------")
    else:
        print("| ERROR! opcion no valida   |")
        print("-----------------------------")