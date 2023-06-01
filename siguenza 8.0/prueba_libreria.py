def suma():
    total_datos = int(input("Ingresa el total de datos a sumar: "))
    suma = 0   
    for i in range(total_datos):
        dato = float(input(f"Ingrese el dato #{i + 1}: "))
        suma += dato
    return suma
def resta():
    total_datos = int(input("Ingresa el total de datos a restar: "))
    for i in range(total_datos):
        resta = 0 
        dato = float(input(f"Ingrese el dato #{i + 1}: ")) 
        resta -= dato
       

    return resta
def multiplicar():
    total_datos = int(input("Ingresa el total de datos a multiplicar: "))
    multiplicar = 1   
    for i in range(total_datos):
        dato = float(input(f"Ingrese el dato #{i + 1}: "))
        multiplicar *= dato
    return multiplicar
def division ():
    validar = False
    while validar != True:     
        a = int(input("Ingrese primer numero: "))
        b = int(input("Ingrese segundo numero: "))
        if a > 0 and b >0:
            division_resul = a/b
            validar = True
        
        else:
            print("No se puede dividir para 0!!!")
    return division_resul



menu = 0
while menu != 5: 
    print("==========CALCULADORA==========")
    print("|[1] Sumar                    |")
    print("|[2] Restar                   |")
    print("|[3] Multiplicar              |")
    print("|[4] Dividir                  |")
    print("|[5] Salir                    |")
    print("===============================")
    menu = int(input("Ingrese una Opcion: "))
    if menu == 1:
        print("SUMA")
        resultado = suma()
        print("La suma de los datos es:", resultado)
    elif menu ==2:
        print("RESTA")
        resultado = resta()
        print("La resta de los datos es:", resultado)
    elif menu ==3:
        print("MULTIPLICACION")  
        resultado = multiplicar()
        print("La multiplicacion de los datos es:", resultado)  
    elif menu ==4:
        print("DIVISION")
        resultado = division()
        print("La division de los datos es:", resultado)  
    elif menu ==5:
        print("Saliendo del Sistema...")
    else:
        "ERROR! opcion no validad pendeje"























