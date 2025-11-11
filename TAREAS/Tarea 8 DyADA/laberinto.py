import pygame
import time

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def leer_laberinto(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = [line.strip() for line in archivo.readlines() if line.strip()]

    filas = int(lineas[0])
    columnas = int(lineas[1])
    laberinto = []
    entrada = salida = None

    for i in range(2, 2 + filas):
        fila = [c.strip().upper() for c in lineas[i].replace(',', ' ').split()]
        laberinto.append(fila)
        for j, celda in enumerate(fila):
            if celda == 'E':
                entrada = (i - 2, j)
            elif celda == 'S':
                salida = (i - 2, j)

    if entrada is None or salida is None:
        raise ValueError("No se encontró una entrada (E) o una salida (S).")
    return laberinto, entrada, salida


def resolver_laberinto(laberinto, entrada, salida, pantalla, tam_celda):
    filas, columnas = len(laberinto), len(laberinto[0])
    visitado = set()
    retroceso = set()
    pila = Pila()
    pila.push(entrada)

    direcciones = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # arriba, izquierda, derecha, abajo

    while not pila.is_empty():
        x, y = pila.peek()
        visitado.add((x, y))

        dibujar_laberinto(pantalla, laberinto, visitado, retroceso, tam_celda)

        if (x, y) == salida:
            return True

        movido = False
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] != '1' and (nx, ny) not in visitado:
                pila.push((nx, ny))
                movido = True
                break

        if not movido:
            retroceso.add(pila.pop())

    return False


def dibujar_laberinto(pantalla, laberinto, visitado, retroceso, tam_celda):
    colores = {
        'pared': (139, 69, 19),      # Café
        'camino': (255, 255, 255),   # Blanco
        'entrada': (0, 255, 0),      # Verde
        'salida': (0, 255, 0),       # Verde
        'visitado': (0, 0, 255),     # Azul
        'retroceso': (255, 0, 0)     # Rojo
    }

    pantalla.fill((0, 0, 0))
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            color = colores['camino']
            if celda == '1':
                color = colores['pared']
            elif celda == 'E':
                color = colores['entrada']
            elif celda == 'S':
                color = colores['salida']
            elif (i, j) in retroceso:
                color = colores['retroceso']
            elif (i, j) in visitado:
                color = colores['visitado']
            pygame.draw.rect(pantalla, color, (j * tam_celda, i * tam_celda, tam_celda - 1, tam_celda - 1))

    pygame.display.flip()
    time.sleep(0.05)


def main():
    nombre_archivo = "laberinto.txt"
    laberinto, entrada, salida = leer_laberinto(nombre_archivo)

    pygame.init()
    tam_celda = 25
    ancho = len(laberinto[0]) * tam_celda
    alto = len(laberinto) * tam_celda
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Laberinto con Backtracking y Pila")

    resolver_laberinto(laberinto, entrada, salida, pantalla, tam_celda)
    terminado = False
    while not terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminado = True

    pygame.quit()


if __name__ == "__main__":
    main()
