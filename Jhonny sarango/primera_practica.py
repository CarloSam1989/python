
print("\nFINONACCI")


def fib(num):
    if num < 2:
        return num
    else:
        # fn = fn-1 + fn-2
        return fib(num - 1) + fib(num - 2)


num1 = int(input("ingrese un numero: "))
for x in range(num1):
    print(fib(x))


# saber si un numero par o impar
print("\nPAR O IMPAR")
num = int(input("ingrese un numero: "))
if (num % 2) == 0:
    print(num, " es par")
else:
    print(num, " es impar")
# indicar cual es el mayor de tres numeros
print("\nEL MAYOR DE TRES NUMEROS")
numeros = []
for i in range(3):
    num = float(input("Introduce el número #{}: ".format(i + 1)))
    numeros.append(num)

mayor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num
print("Mayor:", mayor)

print("\nEL MAYOR DE TRES NUMEROS OTRO METODO")
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
num3 = int(input("ingrese un numero: "))

if num1 > num2 and num2 > num3:
    print(num1, " es mayor")
elif num2 > num1 and num2 > num3:
    print(num2, " es mayor")
elif num3 > num1 and num3 > num2:
    print(num3, " es mayor")


"""edad = input("ingrese la edad: ")
if int(edad) >= 18 and int(edad) < 65:
    print(edad, "mayor de edad")
elif int(edad) >= 65:
    print("es anciano")
elif int(edad) < 18:
    print(edad, "es menor de edad ")
else:
    print(edad, " no es un numero ")
print("-----------------------")
continuar = True
while continuar:
    print("escoga una opcion")
    print("1: suma")
    print("2: resta")
    print("3: multiplicar")
    print("4: dividir")
    print("5: mayor de edad")
    print("6: saber si son iguales")
    print("7:salir")
    print("8: regresar al menu")
    op = int(input("Ingrese una opcion: "))
    if op <= 0:
        print("Ingrese un numero valido")
    elif op == 1:
        print("-----------------------")
        print("suma")
        num = int(input("ingrese un numero: "))
        num2 = int(input("ingrese un numero: "))
        print(num + num2)
        print("-----------------------")
    elif op == 2:
        print("-----------------------")
        print("resta")
        num = int(input("ingrese un numero: "))
        num2 = int(input("ingrese un numero: "))
        print(num - num2)
        print("-----------------------")
    elif op == 3:
        print("-----------------------")
        print("multiplicacion")
        num = int(input("ingrese un numero: "))
        num2 = int(input("ingrese un numero: "))
        print(num * num2)
        print("-----------------------")
    elif op == 4:
        print("-----------------------")
        print("division")
        num = int(input("ingrese un numero: "))
        num2 = int(input("ingrese un numero: "))
        print(num / num2)
        print("-----------------------")
    elif op == 5:
        print("-----------------------")
        print("mayor de edad")
        edad = int(input("ingrese su edad: "))
        if edad >= 18:
            print("es mayor de edad")
            print("-----------------------")
        else:
            print("es menor de edad")
    elif op == 6:
        print("-----------------------")
        print("si son iguales")
        num = int(input("ingrese un numero: "))
        num2 = int(input("ingrese un numero: "))
        if num == num2:
            print("son iguales")
        else:
            print("no son iguales")
        print("-----------------------")
    elif op == 7:
        print("-----------------------")
        print("salir")
        continuar = False
        print("salindo del systema")
        print("-----------------------")
    elif op == 8:
        print("-----------------------")
        print("regresar al menu")
        print("-----------------------")
    else:
        print("ingrese un numero")"""

"""marcas = ["xiaomi", "realme", "iphone", "samsumg", "huawei"]
nombre = input("Ingrese una marca: ")
continuar = True
for x in marcas:
    if nombre == x:
        print(nombre + " si existe")
        continuar = False
        break
    elif nombre != x:
        continuar = True
if continuar == True:
    print("no existe")
""" ""
"""marcas = ""
lista = []
while marcas.lower() != "no":
    if marcas:
        lista.append(marcas)
    marcas = input("desea algo mas :  ")
for x in lista:
    print(x)"""
