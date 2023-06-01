"""
var1 = int(input("Ingrese un valor "))
var2 = int(input("Ingrese otro valor "))
print("La sumatoria es: ", var1+var2)
print("La resta es: ", var1-var2)
print("La multiplicacion es: ", var1*var2)
print("La division es: ", var1/var2)
print("La potencia es: ", var1**var2)
print("La cociente entero es: ", var1//var2)
print("La modulo: ", var1%var2)"""

"""
variable="David Bonilla"
print(variable)
print(variable.find("i"))
"""
"""
b= 65
edad = int(input("Ingrese su edad "))
if edad >= 18 and b <= 64:
    print("mayor de edad")
elif edad > b:
    print("es mayor y viejo")
else:
    print("es menor de edad")"""
"""
print("------------Menu-------------")
print("| 1° Sumar                  |")
print("| 2° Restar                 |")
print("| 3° Multiplicar            |")
print("| 4° Dividir                |")
print("| 5° Mayor edad             |")
print("| 6° Saber si son iguales   |")
print("| 7° Salir                  |")
print("| 8° Regresar Menu          |")
print("-----------------------------")

Selec = int(input("| Seleccione una opcion: "))
print("-----------------------------")

if Selec == 1:
    print("| Suma                      |")
    Val1 = int(input("| Ingrese el 1° Valor: "))
    Val2 = int(input("| Ingrese el 2° Valor: "))
    print("| La sumatoria es: ", Val1+Val2,"      |")
    print("-----------------------------")

if Selec == 2:
    print("| Resta                     |")
    Val1 = int(input("| Ingrese el 1° Valor: "))
    Val2 = int(input("| Ingrese el 2° Valor: "))
    print("| La resta es: ", Val1-Val2,"          |")
    print("-----------------------------")

if Selec == 3:
    print("| Multiplicar               |")
    Val1 = int(input("| Ingrese el 1° Valor: "))
    Val2 = int(input("| Ingrese el 2° Valor: "))
    print("| La multiplicacion es: ", Val1*Val2," |")
    print("-----------------------------")

if Selec == 4:
    print("| Dividir                   |")
    Val1 = int(input("| Ingrese el 1° Valor: "))
    Val2 = int(input("| Ingrese el 2° Valor: "))
    print("| La division es: ", Val1/Val2,"      |")
    print("-----------------------------")

if Selec == 5:
    print("| Mayor de Edad             |")
    b= 65
    edad = int(input("Ingrese su edad "))
    if edad >= 18 and b <= 64:
        print("| Es Mayor de Edad          |")
    elif edad > b:
        print("| Es Mayor de Edad y Viejo  |")
    else:
        print("|Es Menor de Edad           |")
    print("-----------------------------")

if Selec == 6:
    print("| Saber sin son Iguales     |")
    Val1 = int(input("| Ingrese el 1° Valor: "))
    Val2 = int(input("| Ingrese el 2° Valor: "))
    if Val1 == Val2:
        print("Son Iguales")
    else:
        print("No son Iguales")
    print("-----------------------------")

if Selec == 7:
    print("| Salir                     |")
    print("| Saliendo del Sistema...   |")
    print("-----------------------------")

if Selec == 8:
    print("| Regresar Menu             |")
    print("-----------------------------")
"""
"""
Setup = ["a" , "e", "i", "o", "u", "grafica", "altavoces"]
ob_bus = input("")
enc = False
for x in Setup:
    if x==ob_bus:
        enc = True
        break
if enc:
    print("si hay")
else:
    print("no hay")
    """

print("------------Menu-------------")
print("| 1° Opcion 1               |")
print("| 2° Opcion 2               |")
print("| 3° Opcion 3               |")
print("| 4° Salir                  |")
print("-----------------------------")

Selec = int(input("| Seleccione una opcion: "))
print("-----------------------------")

if Selec == 1:
    #presenttar la cantidad de n de la serie de fibonanci
    def fibonacci(n):
        num1 = 0
        num2 = 1
        nums = [num1, num2]
        for i in range(2, n):
            next_num = num1 + num2
            nums.append(next_num)
            num1 = num2
            num2 = next_num
        return nums
    n = int(input("Ingresar el numero maximo de fibonanci: "))
    serie = fibonacci(n)


    # Mostrar la serie de Fibonacci
    print(f"Serie de Fibonacci con {n} números:")
    print(serie)
    print("-----------------------------")

if Selec == 2:
    opc1 = int(input("| Ingrese un número: "))
    if opc1 % 2 == 0:
        print("| Es un número par          |")
        print("-----------------------------")
        
    else:
        print("| Es un número impar        |")
        print("-----------------------------")
        
if Selec == 3:
    print("| Opcion 3                  |")
    opc1 = int(input("| Ingrese un número: "))
    opc2 = int(input("| Ingrese un número: "))
    if opc1 > 3 and opc2 >3:
        print("| Ambos son mayor que 3     |")
    if opc1 > 3 and opc2 <3:
        print("| ",opc1,"es mayor que 3    |")
    if opc1 < 3 and opc2 >3:
        print("| ",opc2,"es mayor que 3    |")
    if opc1 < 3 and opc2 <3:
        print("| Ambos son menores         |")
    print("-----------------------------")


##

