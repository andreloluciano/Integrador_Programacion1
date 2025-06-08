def busqueda_binaria(lista, objetivo):
    izquierda = 0 # incializa el indice izquierdo al comienzo de la lista
    derecha = len(lista) - 1 # inicializa el indice derecho al final de la lista

    while izquierda <= derecha: # mientras el rango de busqueda sea valido
        medio = (izquierda + derecha) // 2 # calcula el indice medio
        if lista[medio] == objetivo:
            return medio  # si encuentra el objetivo, devuelve su indice
        if lista[medio] < objetivo:
            izquierda = medio + 1  # si el objetivo es mayor, descarta la mitad izquierda
        else:
            derecha = medio - 1  # si el obj es menor, descarta la mitad derecha
    return -1  # si no encuentra, devuelve -1

# prueba de la funcion, aqui la lista tiene que estar ordenada
import random

lista = sorted([random.randint(1, 100) for _ in range(10)])
print("Lista ordenada:", lista)

objetivo = int(input("Ingrese el número que desea buscar: "))

indice = busqueda_binaria(lista, objetivo)

if indice != -1:
    print(f"El número {objetivo} se encuentra en el índice {indice}.")
else:
    print(f"El número {objetivo} no está en la lista.")
