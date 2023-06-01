import math
valor = int(input("Ingrese un valor para calcular el factorial: "))

factos = math.factorial(valor)
print("El factorial de {} es: {}".format(valor,factos))


def set_valores(**parametro):
    print(parametro["id"], parametro["nombre"])

set_valores(id="5500", valor="15", nombre="Aaron")


def sumar(*parametro):
    print(parametro)

sumar(5,5)
sumar(5, "valor", 5)
sumar(5,5,4,3,2,4)
