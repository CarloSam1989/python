import math
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

#funciones para calculadora 
print('Calculadora')
print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')
print('5.Salir')

