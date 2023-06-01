

def sumar(*valor):
    return sum(valor)

def restar(a, *valores):
    return a - sum(valores)


def multiplicar(*valores):
    result = 1
    for valor in valores:
        result *= valor
    return result


def residuo(a, b):
    return a % b


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
                num_valores = int(input("Ingrese la cantidad de números que desea sumar: "))
                if num_valores < 2:
                    raise ValueError
                break
            except ValueError:
                print("Error: Ingrese un número entero mayor o igual a 2.")

        valores = []
        for i in range(num_valores):
            while True:
                try:
                    valor = int(input(f"Ingrese el número {i + 1}: "))
                    valores.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número entero.")

        result = sumar(*valores)
        print("------------------")
        print("Su resultado es:", result)
        print("------------------")
    elif operador == 2:
        print("------Resta------")
        while True:
            try:
                num_valores = int(input("Ingrese la cantidad de números que desea restar: "))
                if num_valores < 2:
                    raise ValueError
                break
            except ValueError:
                print("Error: Ingrese un número entero mayor o igual a 2.")

        valores = []
        for i in range(num_valores):
            while True:
                try:
                    valor = int(input(f"Ingrese el número {i + 1}: "))
                    valores.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número entero.")

        result = restar(valores[0], *valores[1:])
        print("Su resultado es:", result)
    elif operador == 3:
        print("------División------")
        while True:
            try:
                num_valores = int(input("Ingrese la cantidad de números para la división: "))
                if num_valores != 2:
                    raise ValueError
                break
            except ValueError:
                print("Error: Ingrese un número entero igual a 2.")

        valores = []
        for i in range(num_valores):
            while True:
                try:
                    valor = int(input(f"Ingrese el número {i + 1}: "))
                    valores.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número entero.")

        if valores[1] != 0:
            result = residuo(valores[0], valores[1])
            print("Su resultado es:", result)
        else:
            print("Error: No se puede dividir por cero")
    elif operador == 4:
        print("------Multiplicación------")
        while True:
            try:
                num_valores = int(input("Ingrese la cantidad de números que desea multiplicar: "))
                if num_valores < 2:
                    raise ValueError
                break
            except ValueError:
                print("Error: Ingrese un número entero mayor o igual a 2.")

        valores = []
        for i in range(num_valores):
            while True:
                try:
                    valor = int(input(f"Ingrese el número {i + 1}: "))
                    valores.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número entero.")

        result = multiplicar(*valores)
        print("Su resultado es:", result)
    elif operador == 5:
        print("------Residuo------")
        while True:
            try:
                num_valores = int(input("Ingrese la cantidad de números para el cálculo del residuo: "))
                if num_valores != 2:
                    raise ValueError
                break
            except ValueError:
                print("Error: Ingrese un número entero igual a 2.")

        valores = []
        for i in range(num_valores):
            while True:
                try:
                    valor = int(input(f"Ingrese el número {i + 1}: "))
                    valores.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número entero.")

        result = residuo(valores[0], valores[1])
        print("Su resultado es:", result)
    elif operador == 6:
        print("------Cociente------")
        while True:
            try:
                num_valores = int(input("Ingrese la cantidad de números para el cálculo del cociente: "))
                if num_valores != 2:
                    raise ValueError
                break
            except ValueError:
                print("Error: Ingrese un número entero igual a 2.")

        valores = []
        for i in range(num_valores):
            while True:
                try:
                    valor = int(input(f"Ingrese el número {i + 1}: "))
                    valores.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número entero.")

        result = cociente(valores[0], valores[1])
        print("Su resultado es:", result)
    elif operador == 7:
        print("------Potencia------")
        while True:
            try:
                num_valores = int(input("Ingrese la cantidad de números para el cálculo de la potencia: "))
                if num_valores != 2:
                    raise ValueError
                break
            except ValueError:
                print("Error: Ingrese un número entero igual a 2.")

        valores = []
        for i in range(num_valores):
            while True:
                try:
                    valor = int(input(f"Ingrese el número {i + 1}: "))
                    valores.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número entero.")

        result = potencia(valores[0], valores[1])
        print("Su resultado es:", result)
    elif operador == 8:
        print("------Calcular Edad------")
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
        print("------Búsqueda entre arreglos------")
        perifericos = {"mouse", "audífonos", "teclado", "monitor"}
        palabra = input("Ingrese la palabra a buscar: ")
        busqueda = [s for s in perifericos if palabra in s]
        print(busqueda)
    elif operador == 10:
        print("Saliendo del sistema...")
        break
    else:
        print("Ingrese una opción válida.")
