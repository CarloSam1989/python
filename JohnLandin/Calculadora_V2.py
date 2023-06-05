

# Primero se pregunta que opcion luego se ingresa numeros y al final se realiza operacion
# Tamano del vector para el ingreso de numeros
tamanoIngreso = int(input("Ingrese la cantidad de numeros a calcular: "))
cantidad = []
for c in range(tamanoIngreso):
    numero = float(input("Ingrese el Numero: "))
    cantidad.append(numero)


def accion1():
    print(cantidad)
    # Imprimimos el resultado y un mensaje de despedida
    print(" La suma es : ", sum(cantidad))
    print("Gracias")


def accion2():
    # Imprimimos el resultado y un mensaje de despedida
    total = cantidad[0]
    for valor in cantidad[1:]:
        total -= valor
    print(" La resta es : ", total)
    print("Gracias")


def accion3():

    # Imprimimos el resultado y un mensaje de despedida
    total = 1
    for valor in cantidad:
        total *= valor
    print(" La multiplicacion es : ", total)
    print("Gracias")


def accion4():
    # Imprimimos el resultado y un mensaje de despedida
    total = cantidad[0]
    for valor in cantidad[1:]:
        total /= valor
    print(" La division es : ", total)
    print("Gracias")


def accion5():
    print('Saliendo')
    raise SystemExit


def leer_opcion(opciones):
    a = int(input('Opción: '))
    if a >= 6:
        print('Opción incorrecta, vuelva a intentarlo.')
    elif a == 1:
        print(a)
        accion1()
    elif a == 2:
        print(a)
        accion2()
    elif a == 3:
        print(a)
        accion3()
    elif a == 4:
        print(a)
        accion4()
    elif a == 5:
        print(a)
        accion5()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        # ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Suma', accion1),
        '2': ('Resta', accion2),
        '3': ('Multiplicacion', accion3),
        '4': ('Division', accion4),
        '5': ('Salir', accion5)
    }

    generar_menu(opciones, '5')


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


if __name__ == '__main__':
    menu_principal()
