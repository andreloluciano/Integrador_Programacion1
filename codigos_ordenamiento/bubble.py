import random
# generamos lista aleatoria
lista_aleatoria = [random.randint(1, 100) for _ in range(10)]
print("Lista aleatoria generada:", lista_aleatoria) # imprimimos la lista ya aca ya que luego se imprime ordenada

def bubble_sort(lista):
    n = len(lista)  # cantidad de valores en la lista

    for i in range(n): # recorre la lista 
        for j in range(0, n - 1): # en cada iteracion, compara pares de valores adyacentes
            if lista[j] > lista[j + 1]: # si el valor actual es mayor que el siguiente, lo intercambia
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # esto asegura que el valor mas alto "suba" al final del array
                
bubble_sort(lista_aleatoria) # aplicamos bubble a la lista
print(f"Lista ordenada con bubble: {lista_aleatoria}")
