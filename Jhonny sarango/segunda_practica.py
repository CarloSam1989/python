def setvalores(**parametro):
    print(parametro["id"])
setvalores(id="123456", valor="5", nombre="hyundai")

import math
valor= int (input("Ingrese un valor para calcular el factorial: "))
factos = math.factorial(valor)
print("El factorial de {} es {}".format(valor,factos))