'''import math
valor= int(input("Ingrese un valor para calcular el factorial: "))
factos= math.factorial(valor)
print( "el factorial de {} es: {}".format(valor, factos))

#calcular la fecha de nacimiento con la actual
import datetime
fecha_actual = datetime.date.today()
fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
fecha_nacimiento = fecha_nacimiento.date()
edad = fecha_actual - fecha_nacimiento
print( "la edad de {} es: {}".format(fecha_nacimiento, edad))
'''
#funciones para calculadora 
def sumar(*num):
    return sum(num)

def restar(*num):
    resultado = num[0]
    for numero in num[1:]:
        resultado -= numero
    return resultado

def multiplicar(*num):
    resultado = 1
    for numero in num:
        resultado *= numero
    return resultado

def dividir(*num):
    if 0 in num[1:]:
        print("!!!ERROR: Eso no se puede dividir. ")
    else:
        resultado = num[0]
        for numero in num[1:]:
            resultado /= numero
            return resultado
while   True:
    print('CALCULADORA')
    print('1. SUMA')
    print('2. RESTA')
    print('3. MULTIPLICACION')
    print('4. DIVISION') 
    print('5. SALIR')

    op= input('Ingrese una opcion:')
    if op == "1":
        cantidad = int(input('Ingrese una cantidad numeros a sumar :'))
        num =   [float(input("El numero que ingrese {}: ".format(i + 1))) for i in range(cantidad)]
        print("Su resultado es: ",sumar(*num))
        
    elif op ==  "2":
        cantidad = int(input('Ingrese una cantidad numeros a restar :'))
        num =   [float(input("El numero que ingrese {}: ".format(i + 1))) for i in range(cantidad)]
        print("Su resultado es: ",restar(*num))

    elif op == "3":
        cantidad = int(input('Ingrese una cantidad numeros a multiplicar :'))
        num =   [float(input("El numero que ingrese {}: ".format(i + 1))) for i in range(cantidad)]
        print("Su resultado es: ", multiplicar(*num))

    elif op == "4":
        cantidad = int(input('Ingrese una cantidad numeros a dividir :'))
        num =   [float(input("El numero que ingrese {}: ".format(i + 1))) for i in range(cantidad)]
        print("Su resultado es: ", dividir(*num))
    elif op == "5":
        print("Adios")
    else:
        print("Opcion incorrecta")
