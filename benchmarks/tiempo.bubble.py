import random
import timeit

def bubble_sort(lista):
    n = len(lista)  # cantidad de valores en la lista

    for i in range(n): # recorre la lista 
        for j in range(0, n - i - 1): # en cada iteracion, compara pares de valores adyacentes
            if lista[j] > lista[j + 1]: # si el valor actual es mayor que el siguiente, lo intercambia
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # esto asegura que el valor mas alto "suba" al final del array

# Generar listas para pruebas (sin caso aleatorio)
lista_mejor_caso = list(range(5000))  # Ordenada (mejor caso)
lista_peor_caso = list(range(5000, 0, -1))  # Orden inverso (peor caso)

# Definir funciones específicas para ejecutar las pruebas
def ejecutar_mejor_caso():
    bubble_sort(lista_mejor_caso[:])

def ejecutar_peor_caso():
    bubble_sort(lista_peor_caso[:])

# Medir tiempos de ejecución
tiempo_mejor = timeit.timeit("ejecutar_mejor_caso()", globals=globals(), number=2) # globals() para que timeit encuentre la función definida
tiempo_peor = timeit.timeit("ejecutar_peor_caso()", globals=globals(), number=2)

print(f"Bubble Sort - Mejor caso (O(n)): {tiempo_mejor:.5f} segundos")
print(f"Bubble Sort - Peor caso (O(n²)): {tiempo_peor:.5f} segundos")