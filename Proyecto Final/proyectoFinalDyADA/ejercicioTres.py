import random
import time

# Funcion para crear listas con numeros aleatorios
def crearListaAleatoria(tamano):
    return [random.randint(1, tamano) for _ in range(tamano)]

# Algoritmo Bubble Sort 
def bubbleSort(lista):
    inicio = time.time()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):

            if time.time() - inicio > 120:
                return "Sobrepasa los 2 minutos de límite"

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return time.time() - inicio

# Algoritmo Selection Sort 
def selectionSort(lista):
    inicio = time.time()
    n = len(lista)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):

            if time.time() - inicio > 120:
                return "Sobrepasa los 2 minutos de límite"

            if lista[j] < lista[minIndex]:
                minIndex = j

        lista[i], lista[minIndex] = lista[minIndex], lista[i]
    return time.time() - inicio

# Algoritmo Merge Sort 
def mergeSort(lista):
    inicio = time.time()

    def mergeSortInterno(arr, inicioProceso):
        
        if time.time() - inicioProceso > 120:
            return None, "Sobrepasa los 2 minutos de límite"

        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            left, mensajeIzq = mergeSortInterno(left, inicioProceso)
            if mensajeIzq:
                return None, mensajeIzq

            right, mensajeDer = mergeSortInterno(right, inicioProceso)
            if mensajeDer:
                return None, mensajeDer

            i = j = k = 0
            while i < len(left) and j < len(right):

                if time.time() - inicioProceso > 120:
                    return None, "Sobrepasa los 2 minutos de límite"

                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr, None

    resultado, mensaje = mergeSortInterno(lista, inicio)
    if mensaje:
        return mensaje
    else:
        return time.time() - inicio

# Bogo Sort 
def bogoSort(lista):
    inicio = time.time()

    def estaOrdenada(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    while not estaOrdenada(lista):
        random.shuffle(lista)

    return time.time() - inicio


# Funcion principal para probar los tamaños
def ejecutarPruebas():
    tamanos = [10, 100, 1000, 10000, 100000]

    for tam in tamanos:
        lista = crearListaAleatoria(tam)
        print(f"\nProbando listas de {tam} elementos:")

        print("Bubble Sort:", bubbleSort(lista.copy()))
        print("Selection Sort:", selectionSort(lista.copy()))
        print("Merge Sort:", mergeSort(lista.copy()))
        
        if tam <= 10:  # Solo permitir BogoSort en listas muy pequeñas
            print("BogoSort:", bogoSort(lista.copy()))
        else:
            print("BogoSort: Demasiado lento ")

ejecutarPruebas()
