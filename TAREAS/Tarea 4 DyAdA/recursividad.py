# Ejercicio 1: Suma recursiva de lista
def sumaListaRecursiva(nums):
    if not nums:  #
        return 0
    return nums[0] + sumaListaRecursiva(nums[1:])

valores = [5, 7, 2, 4]
print(" EJERCICIO 1 ")
print("Lista:", valores)
print("Suma total:", sumaListaRecursiva(valores))
print("\n")  



# Ejercicio 2: Contar dígitos de un número

def contarDigitos(num):
    if num < 10: 
        return 1
    return 1 + contarDigitos(num // 10)

numero = 58839
print(" EJERCICIO 2 ")
print("Número:", numero)
print("Cantidad de dígitos:", contarDigitos(numero))
print("\n")

# Ejercicio 3: Eliminar el valor en la posición media de una pila

class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, valor):
        self.elementos.append(valor)

    def pop(self):
        if self.estaVacia():
            return None
        return self.elementos.pop()

    def estaVacia(self):
        return len(self.elementos) == 0

    def eliminarMedio(self):
        if self.estaVacia():
            return
        posicionMedia = len(self.elementos) // 2
        self._eliminarRecursivo(posicionMedia)

    def _eliminarRecursivo(self, pos):
        if pos == 0:
            self.pop()
            return
        dato = self.pop()
        self._eliminarRecursivo(pos - 1)
        self.push(dato)

print(" EJERCICIO 3 ")
pila = Pila()
for v in [10, 20, 30, 40, 50]:
    pila.push(v)
print("Antes de eliminar:", pila.elementos)
pila.eliminarMedio()
print("Después de eliminar:", pila.elementos)
print("\n")

# Ejercicio 4: Verificar si una cadena es palíndromo

def esPalindromoRecursivo(cadena):
    if len(cadena) <= 1:  
        return True
    if cadena[0] != cadena[-1]:
        return False
    return esPalindromoRecursivo(cadena[1:-1])

texto = "reconocer"
print("EJERCICIO 4 ")
print(f"¿'{texto}' es palíndromo?:", esPalindromoRecursivo(texto))
