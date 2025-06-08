def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i # devuelve el indice donde se encontro
    return -1 #si no se encuentra, devuelve -1

# codigo para probar la funcion
import random

lista = [random.randint(1, 100) for _ in range(100)]

objetivo = int(input("Ingrese un numero del 1 al 100: ")) #valor a buscar

indice = busqueda_lineal(lista, objetivo) # busqueda

# muestra resultado
if indice != -1:
    print(f"El valor {objetivo} se encontró en la posición {indice}")
else:
    print(f"El valor {objetivo} no se encuentra en la lista")