from datetime import datetime, date

actual = datetime.now()


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def residuo(a, b):
    return a % b


def division(a, b):
    return a / b


def cociente(a, b):
    return a // b


def potencia(a, b):
    return a ** b


def edad(a, b):
    return a - b


while True:
    print("------------------")
    print("-----MENU----")
    print(" 1. SUMAR")
    print(" 2. RESTA")
    print(" 3. DIVISION")
    print(" 4. MULTIPLICACION")
    print(" 5. RESIDUO")
    print(" 6. COCIENTE")
    print(" 7. POTENCIA")
    print(" 8. CALCULAR EDAD")
    print(" 9. BUSQUEDA ENTRE ARREGLOS")
    print(" 10. SALIR")
    print("------------------")
    while True:
        try:
            operador = int(input("Seleccione una opción: "))
            break
        except ValueError:
            print("Error: Ingrese un número entero.")

    if operador == 1:
        print("------Suma------")
        while True:
            try:
                numero1 = int(input("Ingrese el primer número: "))
                numero2 = int(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Ingrese números enteros.")
        result = sumar(numero1, numero2)
        print("------------------")
        print("Su resultado es:", result)
        print("------------------")
    elif operador == 2:
        print("------Resta------")
        while True:
            try:
                numero1 = int(input("Ingrese el primer número: "))
                numero2 = int(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Ingrese números enteros.")
        result = restar(numero1, numero2)
        print("Su resultado es:", result)
    elif operador == 3:
        print("------Division------")
        while True:
            try:
                numero1 = int(input("Ingrese el primer número: "))
                numero2 = int(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Ingrese números enteros.")
        if numero2 != 0:
            result = division(numero1, numero2)
            print("Su resultado es:", result)
        else:
            print("Error: No se puede dividir por cero")
    elif operador == 4:
        print("------Multiplicacion------")
        while True:
            try:
                numero1 = int(input("Ingrese el primer número: "))
                numero2 = int(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Ingrese números enteros.")
        result = multiplicar(numero1, numero2)
        print("Su resultado es:", result)
    elif operador == 5:
        print("------Residuo------")
        while True:
            try:
                numero1 = int(input("Ingrese el primer número: "))
                numero2 = int(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Ingrese números enteros.")
        result = residuo(numero1, numero2)
        print("Su resultado es:", result)
    elif operador == 6:
        print("------Cociente------")
        while True:
            try:
                numero1 = int(input("Ingrese el primer número: "))
                numero2 = int(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Ingrese números enteros.")
        result = cociente(numero1, numero2)
        print("Su resultado es:", result)
    elif operador == 7:
        print("------Potencia------")
        while True:
            try:
                numero1 = int(input("Ingrese un número: "))
                numero2 = int(input("Ingrese el exponente: "))
                break
            except ValueError:
                print("Error: Ingrese números enteros.")
        result = potencia(numero1, numero2)
        print("Su resultado es:", result)
    elif operador == 8:
        print("------CALCULAR EDAD------")
        while True:
            try:
                numero1 = int(input("Ingrese el año de nacimiento: "))
                numero2 = int(input("Ingrese el año actual: "))
                break
            except ValueError:
                print("Error: Ingrese números enteros.")
        result = edad(numero1, numero2)
        print("Su edad es:", result, " años")
    elif operador == 9:
        print("------BUSQUEDA ENTRE ARREGLOS------")
        perifericos = {"mouse", "audifonos", "teclado", "monitor"}
        palabra = input("Ingrese palabra a buscar: ")
        busqueda = [s for s in perifericos if palabra in s]
        print(busqueda)
    elif operador == 10:
        print("Saliendo del sistema...")
        break
    else:
        print("Ingrese una opción válida.")
