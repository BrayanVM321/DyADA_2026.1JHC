def existe_par_hash_v2(A, K):
    vistos = {}
    n = len(A)

    for i in range(n):

        complemento = K - A[i]

        if complemento in vistos:

            return True
        
        vistos[A[i]] = True
    
    return False

nums = [5, 2, 3, 7, 9]
objetivo = 8
print(existe_par_hash_v2(nums, objetivo)) 

#version 2 del algoritmo 

def existe_par_dos_arreglos_v2(A, K):
    
    B = sorted(A)
    izq = 0
    der = len(B) - 1

    while izq < der:
        suma_actual = B[izq] + B[der]
        if suma_actual == K:
            return True
        if suma_actual < K:
            izq += 1
        else:
            der -= 1
    return False

nums = [5, 2, 3, 7, 9]
objetivo = 8 
print(existe_par_dos_arreglos_v2(nums, objetivo)) 