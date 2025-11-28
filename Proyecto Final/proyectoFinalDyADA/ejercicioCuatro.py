def cargar_postes(nombre):
    postes = []
    with open(nombre, "r", encoding="utf-8") as f:
        for linea in f:
            x, y = map(int, linea.split())
            if x == -1 and y == -1:
                break
            postes.append((x, y))
    return postes


def area(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2


def fuerza_bruta(postes):
    n = len(postes)
    total_triangulos = n * (n - 1) * (n - 2) // 6

    print("Postes:", n)
    print("Total de triángulos posibles:", total_triangulos)

    """Aqui detectamos que para n=500 se generarían más de 20 millones
     de triángulos. Esa cantidad es demasiado grande para evaluarse
     dentro de un tiempo razonable en Python por eso se detiene"""
    
    if total_triangulos > 1_000_000:
        print("\nEl proceso por fuerza bruta se detiene aquí.")
        print("La cantidad de triángulos supera un límite práctico para Python.")
        return None

    # Si fueran pocos elementos aquí irían los 3 ciclos 
  
    return None


if __name__ == "__main__":
    postes = cargar_postes("campo.in")
    fuerza_bruta(postes)
