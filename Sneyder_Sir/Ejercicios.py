from colorama import Fore,Back,Style 
#Presentar la Cantidad n de la serie de Fibonacci
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