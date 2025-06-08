# codigo del colab (recursivo) (el mas amigable)
import random

lista = [random.randint(1, 100) for _ in range(10)]
print(f"Lista aleatoria original:{lista}") # imprimimos lista original

def quicksort(arr):
    if len(arr) <= 1:  # caso base una lista de 0 o 1 elemento ya está ordenada
        return arr
    else:
        pivot = arr[0]  # elige el primer elemento como pivote
        less = [x for x in arr[1:] if x <= pivot] # crea una lista con todos los elementos menores o iguales al pivote
        greater = [x for x in arr[1:] if x > pivot] # creamos una lista con todos los elementos mayores al pivote      
        return quicksort(less) + [pivot] + quicksort(greater)  # aplica quicksort recursivamente y combinamos los resultados

# quicksort a la lista
lista_ordenada = quicksort(lista)
print(f"Lista ordenada:{lista_ordenada}")

