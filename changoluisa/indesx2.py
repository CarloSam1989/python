#presentar la cantidad n de la serie de fibonacci
a=0
b=1
c=0
while True:
    n=int(input("Ingrese un numero "))
    if n > 1:
        break
print( '1', end=" ")
for i in range (0 ,n):
    c=a+b
    print(f"{c}" , end=" ")
    a=b
    b=c
    print("")

#saber si numero es par  o impar 
var = int(input('Ingrese un numero:'))
if var % 2==0 :
    print(var, 'Es par')
else:
    print(var, 'Es impar')

#indicar cual es el mayor 3 numeros
def nummayor(num1,num2,num3):
    a = max(num1,num2,num3)
    return a 
var= int(input("Ingrese el primer numero:"))
var2= int(input("Ingrese el segundo numero:"))
var3= int(input("Ingrese el tercer numero:"))
Mostrar = nummayor(var,var2,var3)
print("el numero es mayor" , Mostrar)
