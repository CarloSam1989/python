# con el asterisco se pueden ingresar n parametros
# cuando tiene 2 * recibe valores distintos para llamar a un objeto
def setvalores(**parametro):
    print(parametro["nombre"])


setvalores(id="15638", valor="5", nombre="john landin")
