def suma(*numero):
    parametro = None
    resultado = numero + parametro
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
        sumafinal = 0
        for x in suma:
            sumafinal = sumafinal + x
        print(sumafinal)
    elif int(opcion) == 2:
        veces = int(input("Ingrese la cantidad de numeros que desea restar: "))
        resta = []
        for i in range(veces):
            numero = float(input("Introduce el número #{}: ".format(i + 1)))
            resta.append(numero)
        restafinal = 0
        for x in resta:
            restafinal = restafinal - x
        print(restafinal)
    elif int(opcion) == 3:
        veces = int(input("Ingrese la cantidad de numeros que desea multiplicar: "))
        multiplica = []
        for i in range(veces):
            numero = float(input("Introduce el número #{}: ".format(i + 1)))
            multiplica.append(numero)
        multiplicafinal = 1
        for x in multiplica:
            multiplicafinal = multiplicafinal * x
        print(multiplicafinal)
    elif int(opcion) == 4:
        print("Hasta luego")
        salir = False
    else:
        print("No es un número")
