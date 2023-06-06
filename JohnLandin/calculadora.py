# hacer una calculadora , operaciones basicas , y poder subir mas de un numero para que sume todo

# calculadora basica.
# solicitar al usuario 2 numeros y relaizar la suma de ellos

# declaramos las variables
# utilizamos input para quese guarde lo que el usuario ingresa
num1 = float(input("Ingrese un Numero: "))
num2 = float(input("ingrese otro numero: "))

res1 = num1 + num2
res2 = num1 - num2
res3 = num1 * num2
res4 = num1 / num2

# menu de opciones basicas


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Suma', accion1),
        '2': ('Resta', accion2),
        '3': ('Multiplicacion', accion3),
        '4': ('Division', accion4),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def accion1():

    # Imprimimos el resultado y un mensaje de despedida
    print(" La suma es : ", res1)
    print("Gracias")


def accion2():

    # Imprimimos el resultado y un mensaje de despedida
    print(" La resta es : ", res2)
    print("Gracias")


def accion3():

    # Imprimimos el resultado y un mensaje de despedida
    print(" La multiplicacion es : ", res3)
    print("Gracias")


def accion4():

    # Imprimimos el resultado y un mensaje de despedida
    print(" La division es : ", res4)
    print("Gracias")


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()

"""# declaramos las variables
# utilizamos input para quese guarde lo que el usuario ingresa
num1 = float(input("Ingrese un Numero: "))
num2 = float(input("ingrese otro numero: "))

# Realizamos la suma y guardamos el resultado

res = num1 + num2

# Imprimimos el resultado y un mensaje de despedida
print(" La suma es : ", res)
print("Gracias")"""
