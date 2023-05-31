"""print("Suma")
var = int(input("Ingrese un numero: "))
var2=int(input("ingrese otro nmero:"))
print("la suma es:",var+var2)
print("Resta")
var = int(input("Ingrese un numero: "))
var2=int(input("ingrese otro nmero:"))
print("la Resta es:",var-var2)
print("Multiplicacion")
var = int(input("Ingrese un numero: "))
var2=int(input("ingrese otro nmero:"))
print("la Multiplicacion es:",var*var2)
print("Divicion")
var = int(input("Ingrese un numero: "))
var2=int(input("ingrese otro nmero:"))
print("la Divicion es:",var/var2)
print("Potencia")
var = int(input("Ingrese un numero: "))
var2=int(input("ingrese otro nmero:"))
print("El Potencia es:",var%var2)
print("Modulo")
var = int(input("Ingrese un numero: "))
var2=int(input("ingrese otro nmero:"))
print("la Modulo es:",var**var2)
print("cociente entero")
var = int(input("Ingrese un numero: "))
var2=int(input("ingrese otro nmero:"))
print("El cociente entero es:",var//var2)
variable="darwin"
print(variable)
print(variable[0:5])
a=1+1
b=2
if a==b:
    print("es igual")
else:
    print("mi perro")
print("la queso")
while True:
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("Eres mayor de edad.")
        break
    else:
        print("Eres menor de edad. Intente nuevamente.")

print("Fin del programa.")


while True:
    opcion = int(input("Seleccione una opción:\n1. Ingresar nombre\n2. Ingresar edad\n3. Suma\n4. Resta\n5. Multiplicación\n6. División\n7.  Salir\nOpción: "))

    if opcion == 1:
        nombre = input("Ingrese su nombre: ")
        print("Nombre ingresado:", nombre)
    elif opcion == 2:
        edad = int(input("Ingrese su edad: "))
        if edad >= 18:
            print("Eres mayor de edad.")
        else:
            print("Eres menor de edad.")
    elif opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if opcion == 3:
            resultado = num1 + num2
            print("El resultado de la suma es:", resultado)
        elif opcion == 4:
            resultado = num1 - num2
            print("El resultado de la resta es:", resultado)
        elif opcion == 5:
            resultado = num1 * num2
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == 6:
            if num2 != 0:
                resultado = num1 / num2
                print("El resultado de la división es:", resultado)
            else:
                print("No se puede dividir entre cero.")
    elif opcion == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. ingrese una opción válida.\n")




palabras = ["mouse", "monitor", "teclado"]
onta_p=input ("")
ch=False
for x in palabras:
    if x==onta_p:
        ch = True
        break
    if ch:
        print("si hay")
    else: 
        print("no hay")

        user_input =''
        lista=[]
        while user_input.lower() !='ya'
        if user_input:
            lista.append(user_input)
user_input = input('escriba algo, si kiere salir ya:: ')
for x in lista:
    print(x)"""


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



#saber si un numero espar o inpar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
numero = int(input("Ingrese un número: "))
if es_par(numero):
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.")
    # indicar cual es el mayor de 3 numeros

def encontrar_mayor(a, b, c):
    return max(a, b, c)
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

mayor = encontrar_mayor(num1, num2, num3)
print("El número mayor es:", mayor)
