import timeit
import random

def selection_sort(lista):
    n = len(lista)  # guardamos la cantidad de valores
    for i in range(n - 1):  # itera hasta el anteúltimo elemento
        min_indice = i  # guarda el valor actual como el mínimo
        for j in range(i + 1, n):  # bucle interno busca el menor valor restante
            if lista[j] < lista[min_indice]:
                min_indice = j  # reemplaza el valor mínimo si es más chico
        lista[i], lista[min_indice] = lista[min_indice], lista[i]  # intercambia valores
    return lista  # devuelve la lista ordenada

# Generar listas de prueba
lista_mejor_caso = list(range(5000))  # lista ordenada (mejor caso)
lista_peor_caso = list(range(5000, 0, -1))  # lista en orden inverso (peor caso)

# definimos funciones para ejecutar las pruebas
def ejecutar_mejor_caso():
    selection_sort(lista_mejor_caso[:])

def ejecutar_peor_caso():
    selection_sort(lista_peor_caso[:])

# Medir tiempos de ejecución
tiempo_mejor = timeit.timeit("ejecutar_mejor_caso()", globals=globals(), number=2) # globals() para que timeit encuentre la función definida
tiempo_peor = timeit.timeit("ejecutar_peor_caso()", globals=globals(), number=2)

print(f"Selection Sort - Mejor caso (O(n²)): {tiempo_mejor:.5f} segundos")
print(f"Selection Sort - Peor caso (O(n²)): {tiempo_peor:.5f} segundos")