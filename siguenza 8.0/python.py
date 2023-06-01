"""____________________FUNCIONES____________________________"""
def fibonacci(n):
    fib = []
    a, b = 0, 1
    while len(fib) < n:
        fib.append(a)
        a, b = b, a + b
    return fib

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def encontrar_mayor(num1, num2, num3):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
    return mayor
"""_________________________________________________________"""




while True:
    print("=====Menú=====")
    print("1. Ejercicio #1")
    print("2. Ejercicio #2")
    print("3. Ejercicio #3")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("_____Presentar la cantidad N de la serie de Fibonacci_____")
        numero = int(input("Ingrese un número para generar la serie de Fibonacci: "))   
        serie_fibonacci = fibonacci(numero)
        print("La serie de Fibonacci hasta el número", numero, "es:", serie_fibonacci)

    elif opcion == "2":
        print("_____Saber si un numero es par o impar_____")
        numero = int(input("Ingrese un número: "))
        if es_par(numero):
         print(numero, "es un número par.")
        else:
         print(numero, "es un número impar.")

    elif opcion == "3":
        print("_____Indicar cual es el mayor de 3 numeros_____")
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        numero3 = int(input("Ingrese el tercer número: "))

        mayor = encontrar_mayor(numero1, numero2, numero3)
        print("El mayor de los tres números es:", mayor)

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida!! pendejo:v")


        


