def area1(a, b, c):
    ax = a[0] * (b[1] - c[1])
    bx = b[0] * (c[1] - a[1])
    cx = c[0] * (a[1] - b[1])
    return abs(ax + bx + cx)

# Funcion para saber como estan orientados tres puntos
def orientacion(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

# Convex hull (algoritmo monotone chain pero escrito como lo entendi)
def convex_hull(puntos):
    puntos = sorted(puntos)

    if len(puntos) <= 1:
        return puntos

    abajo = []
    for p in puntos:
        while len(abajo) >= 2 and orientacion(abajo[-2], abajo[-1], p) <= 0:
            abajo.pop()
        abajo.append(p)

    arriba = []
    for p in reversed(puntos):
        while len(arriba) >= 2 and orientacion(arriba[-2], arriba[-1], p) <= 0:
            arriba.pop()
        arriba.append(p)

    # Como el ultimo se repite no lo puse
    return abajo[:-1] + arriba[:-1]

# Buscar el triangulo de mayor area entre los puntos del hull
def triangulo_max_area(hull):
    n = len(hull)
    if n < 3:
        print("No alcanza para un triangulo :(")
        return None

    mayor = 0
    mejor_triangulo = None

    for i in range(n):
        k = i + 2
        for j in range(i + 1, n):
            if k >= n:
                k = n - 1

            # voy moviendo k mientras aumente el area
            while k + 1 < n and area1(hull[i], hull[j], hull[k + 1]) > area1(hull[i], hull[j], hull[k]):
                k = k + 1

            area_actual = area1(hull[i], hull[j], hull[k])

            if area_actual > mayor:
                mayor = area_actual
                mejor_triangulo = (hull[i], hull[j], hull[k])

    return mejor_triangulo, mayor / 2.0

def main():
    archivo = "campo.in"

    f = open(archivo, "r")
    puntos = []
    for linea in f:
        x, y = map(float, linea.split())
        puntos.append((x, y))
    f.close()

    # Sacar convex hull
    hull = convex_hull(puntos)
    print("Hull calculado:")
    print(hull)

    # Triangulo mayor
    resultado = triangulo_max_area(hull)
    if resultado is None:
        return

    triangulo, area = resultado

    print("Triangulo de mayor area encontrado:")
    print(triangulo)
    print("Area:", area)

main()
