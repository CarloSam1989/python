"""def setvalores(**parametro):
    print(parametro["id"])
setvalores(id="123456", valor="5", nombre="hyundai")

import math
valor= int (input("Ingrese un valor para calcular el factorial: "))
factos = math.factorial(valor)
print("El factorial de {} es {}".format(valor,factos))


from datetime import date, timedelta

print(date.today())  """""
def suma(*numeros):
   return sum(numeros)

def restar(*numeros):
   resultado = numeros[0]
   for num in numeros[1:]:
     resultado -= num
     return resultado

def multiplicar(*numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
     resultado *= num
     return resultado

def dividir(*numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
     resultado /= num
     return resultado
continuar=True
while continuar:
    print("----------MENU----------")
    print("1: sumar")
    print("2: restar")
    print("3: multiplicar")
    print("4: dividir")
    print("5: salir del sytema")
    print("-------------------------")
    opcion = input("Ingrese una opción: ")
    print("-------------------------")
    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad de números a sumar: "))
        print("-------------------------")
        numeros = [float(input("Ingrese un número {}: ".format(i+1))) for i in range(cantidad)]
        print("El resultado es:", suma(*numeros))
    if opcion == "2":
        cantidad = int(input("Ingrese la cantidad de números a restar: "))
        print("-------------------------")
        numeros = [float(input("Ingrese un número {}: ".format(i+1))) for i in range(cantidad)]
        print("El resultado es:", restar(*numeros))
    if opcion == "3":
        cantidad = int(input("Ingrese la cantidad de números a multiplicar: "))
        print("-------------------------")
        numeros = [float(input("Ingrese un número {}: ".format(i+1))) for i in range(cantidad)]
        print("El resultado es:", multiplicar(*numeros))
    if opcion == "4":
        cantidad = int(input("Ingrese la cantidad de números a dividir: "))
        print("-------------------------")
        numeros = [float(input("Ingrese un número {}: ".format(i+1))) for i in range(cantidad)]
        print("El resultado es:", dividir(*numeros))        
    if opcion == "5":
       print("salir del systema")
       continuar=False

"""""
continuar=True
while continuar:
    valor= int (input("Ingrese la cantidad de numeros que desea operar : "))
    print("escoga una opcion: ")
    print("1: sumar")
    print("2: restar")
    print("3: multiplicar")
    print("4: dividir")
    print("5: salir del sytema")
    op = int(input("Ingrese una opcion: "))
    if op <= 0:
        print("Ingrese un numero valido")
    elif op == 1:
        print("-----------------------")
        print("suma")
        sum = []
        for i in range(valor):
            num = float(input("Introduce el número #{}: ".format(i + 1)))
            sum.append(num)
        suma = 0   
        for x in sum:
            suma  = suma + x
        print(suma)
        print("-----------------------")
    elif op == 2:
        print("-----------------------")
        print("resta")
        rest = []
        for i in range(valor):
            num = float(input("Introduce el número #{}: ".format(i + 1)))
            rest.append(num)
        resta = 0   
        for x in rest:
            resta = resta - x
        print(resta)
        
        print("-----------------------")
    elif op == 3:
        print("-----------------------")
        print("multiplicacion")
        multi = []
        for i in range(valor):
            num = float(input("Introduce el número #{}: ".format(i + 1)))
            multi.append(num)
        multiplicar = 1   
        for x in multi:
            multiplicar  = multiplicar * x
        print(multiplicar)
        
        print("-----------------------")
    elif op == 4:
        print("-----------------------")
        print("division")
        div = []
        for i in range(valor):
            num = float(input("Introduce el número #{}: ".format(i + 1)))
            div.append(num)
        division = 0   
        for x in div:
            division  /=x
        print(division)
       
        print("-----------------------")
    elif op == 5:
        print("-----------------------")
        print("salir")
        continuar = False
        print("salindo del systema")
        print("-----------------------")    
    else:
        print("no es una opcion valida")"""





