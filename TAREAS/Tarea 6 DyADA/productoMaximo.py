def producto_maximo(arr, inicio, fin):
    
    if inicio == fin:
        return arr[inicio]

    
    medio = (inicio + fin) // 2

    
    max_izq = producto_maximo(arr, inicio, medio)
    max_der = producto_maximo(arr, medio + 1, fin)

   
    max_cruzado = producto_cruzado(arr, inicio, medio, fin)

    
    return max(max_izq, max_der, max_cruzado)


def producto_cruzado(arr, inicio, medio, fin):
    
    prod_temp = 1
    mejor_izq = float('-inf')
    for i in range(medio, inicio - 1, -1):
        prod_temp *= arr[i]
        if prod_temp > mejor_izq:
            mejor_izq = prod_temp

    
    prod_temp = 1
    mejor_der = float('-inf')
    for j in range(medio + 1, fin + 1):
        prod_temp *= arr[j]
        if prod_temp > mejor_der:
            mejor_der = prod_temp

    
    return mejor_izq * mejor_der



if __name__ == "__main__":
    arreglo = [9, 1, 4, -1, 0, 1, 5, 8]
    resultado = producto_maximo(arreglo, 0, len(arreglo) - 1)
    print("El producto máximo es:", resultado)
