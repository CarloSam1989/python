listas = ["Sarango", "Aaron", "Landin", "García", "Tinoco"]
print(listas)
listas.insert(2, "changololuisa") #inserta en una possicon determinada
print(listas)
listas.append("siguenza") #inserta al final
print(listas)
listas.remove("Aaron") #elimina por texto
print(listas)
listas.pop(0) #elimina por index
print(listas)
del listas[1] #elimina por index
print(listas)
listas.clear() #elimina toda la lista
print(listas)
listas = ["Sarango", "Aaron", "Landin", "García", "Tinoco"]
listas.sort() #Ordena de mayor a menor
print(listas)
listas.sort(reverse=True) #Ordena de menor a mayor
print(listas)
arreglo = sorted(listas) #Ordena de mayor a menor en otro arreglo
print(listas)
print(arreglo)