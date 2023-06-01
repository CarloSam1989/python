def sumar(*numeros):
    resultado = sum(numeros)
    return resultado
def restar(*numeros):
    resultado = numeros[0]
    for x in numeros[1:]:
        resultado -= x
    return resultado
def multiplicar(*numeros):
    resultado = 1
    for x in numeros:
        resultado *= x
    return resultado
salir = True
while salir:
    print("\n1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Salir")
    
    opcion = input("-->")
    if int(opcion) == 1:
        veces = int(input("Ingrese la cantidad de numeros que desea sumar: "))
        suma = []
        for i in range(veces):
            numero = float(input("Introduce el número #{}: ".format(i + 1)))
            suma.append(numero)
        resultado = sumar(*suma)
        print("El resultado de la suma es:", resultado)
    elif int(opcion) == 2:
        veces = int(input("Ingrese la cantidad de numeros que desea restar: "))
        resta = []
        for i in range(veces):
            numero = float(input("Introduce el número #{}: ".format(i + 1)))
            resta.append(numero)
        resultado = restar(*resta)
        print("El resultado de la resta es:", resultado)
    elif int(opcion) == 3:
        veces = int(input("Ingrese la cantidad de numeros que desea multiplicar: "))
        multiplica = []
        for i in range(veces):
            numero = float(input("Introduce el número #{}: ".format(i + 1)))
            multiplica.append(numero)
        resultado = multiplicar(*multiplica)
        print("El resultado de la resta es:", resultado)
    elif int(opcion) == 4:
        print("Hasta luego")
        salir = False
    else:
        print("No es un número")
