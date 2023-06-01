from colorama import Fore, Back, Style
'''

def sumar(*parametros):
    resultado = sum(parametros)
    return resultado


def dividir(*parametros):
    resultado = parametros[0]
    for parametro in parametros[1:]:
        resultado /= parametro
    return resultado


def multiplicar(*parametros):
    resultado = 1
    for parametro in parametros:
        resultado *= parametro
    return resultado


def restar(*parametros):
    resultado = parametros[0]
    for parametro in parametros[1:]:
        resultado -= parametro
    return resultado

# Definir la función del menú principal


def menuPrinc():
    print('***Menu***')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')

    opcion = int(input('Ingrese la opción que desea ejecutar: '))

    if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
        cantidad_ingreso = int(
            input('Ingrese la cantidad de números a ingresar: '))
        numeros = []
        for e in range(cantidad_ingreso):
            numero = float(input('Ingrese el número {}: '.format(e + 1)))
            numeros.append(numero)

        if opcion == 1:
            resultado = sumar(*numeros)
            print("El resultado de la suma es:", resultado)
        elif opcion == 2:
            resultado = restar(*numeros)
            print("El resultado de la resta es:", resultado)
        elif opcion == 3:
            resultado = multiplicar(*numeros)
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == 4:
            resultado = dividir(*numeros)
            print("El resultado de la división es:", resultado)

    elif opcion != 4:
        print("Opción inválida. Por favor, elige una opción válida del menú.")


menuPrinc()


def fibonacci(n):
    if n <= 0:
        print("El valor de 'n' debe ser un número entero positivo.")
        return

    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_term)

    print(f"La serie de Fibonacci para n = {n} es: {fibonacci_sequence}")
#Saber si un numero es par o impar
def verficNam(num):
    if(num)%2==0:
        print('El numero es par')
    else:
        print('El numero es Impar')


#Indicar cual es el mayor de 3 numeros
def MayorMenor(num1,num2,num3):
    almacenTop = max(num1,num2,num3)
    return almacenTop

print(Fore.GREEN+'1-Ejercicio de Si es numero par o impar'+Fore.RESET)
varIngreso = int(input("Ingrese el numero: "))
verficNam(varIngreso)
print(Fore.GREEN+'2-Ejercicio de Si un numero es mayor'+Fore.RESET)
ingresopart0= int(input('Ingrese el primer numero:'))
ingresopart1= int(input('Ingrese el segundo numero:'))
ingresopart2= int(input('Ingrese el tercer numero:'))
Designado = MayorMenor(ingresopart0,ingresopart1,ingresopart2)
print('El numero mayor es ',Designado)
print(Fore.GREEN+'3-Ejercicio de Fibonacci'+Fore.RESET)
nanox = int(input('Ingrese un numero entero positivo: '))
fibonacci(nanox)
'''


def datePeople(**parametro):
    print(parametro["nombre"], parametro['id'], parametro['valor'])


datePeople(id='1223', valor='20$', nombre='RedmiNote7')

mensaje = 'Tener una influencia'
for numero in range(0, 5):
    print(numero)


def suma_parametros(*autentic):
    resultado = 0
    for num in autentic:
        resultado += num
    return resultado


def ingreso_paremetros():
    parametro = []
    a = 1
    while True:

        ingreso = input("Ingrese el parámetro  {} (enter con valor vacio para finalizar) ".format(
            a))
        a += 1
        if ingreso == "":
            break
        try:
            parametro = int(ingreso)
            parametros.append(parametro)
        except ValueError:
            print("¡Error! Ingrese valor numerico valido")
    return parametro


parametros = ingreso_paremetros()
resultado = suma_parametros(*parametros)
