print("Presentar la cantidad N de la serie fibonachi")
def fibonacci_iterativo(posicion, debe_imprimir):
    actual = 1
    siguiente = 1
    print("0, 1", end="")
    for x in range((posicion-1)):
        temporal = actual
        actual = siguiente
        siguiente = siguiente + temporal
        if debe_imprimir:
            print(",", str(actual), end="")
    return temporal


serie = int(input("Ingrese cuántos numeros de la serie quiere presentar: "))
fibonacci_iterativo(serie, True)

print("\nPresentar si un numero es par o impar")
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")

print("Presentar el mayor de tres números")
numeros = []
for i in range(3):
    numero = float(input("Introduce el número #{}: ".format(i + 1)))
    numeros.append(numero)
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
print("Mayor:", mayor)
