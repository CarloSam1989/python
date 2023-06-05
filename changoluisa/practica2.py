"""def setvalores(**parametro):
    print(parametro["id"])
    setvalores(id="12343",valor="5",nombre="hyundai")

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2)"""



def sumar(*numeros):
    return sum(numeros)

def restar(*numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicar(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def dividir(*numeros):
    if 0 in numeros[1:]:
        print(" No se puede dividir entre cero.")
    else:
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado /= num
        return resultado

while True:
    print("Calculadora Z ")
    print("---------1. Sumar-------------")
    print("---------2. Restar------------")
    print("---------3. Multiplicar-------")
    print("---------4. Dividir-----------")
    print("---------5. Salir-------------")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad de números a sumar: "))
        numeros = [float(input("Ingrese un número {}: ".format(i+1))) 
                   for i in range(cantidad)]
        print("El resultado es:", sumar(*numeros))
    elif opcion == "2":
        cantidad = int(input("Ingrese la cantidad de números a restar: "))
        numeros = [float(input("Ingrese un número {}: ".format(i+1))) for i in range(cantidad)]
        print("El resultado es:", restar(*numeros))
    elif opcion == "3":
        cantidad = int(input("Ingrese la cantidad de números a multiplicar: "))
        numeros = [float(input("Ingrese un número {}: ".format(i+1))) for i in range(cantidad)]
        print("El resultado es:", multiplicar(*numeros))
    elif opcion == "4":
        cantidad = int(input("Ingrese la cantidad de números a dividir: "))
        numeros = [float(input("Ingrese un número {}: ".format(i+1))) for i in range(cantidad)]
        resultado = dividir(*numeros)
        if resultado:
            print("El resultado es:", resultado)
    elif opcion == "5":
        print("¡Adiós vaquero :v!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

