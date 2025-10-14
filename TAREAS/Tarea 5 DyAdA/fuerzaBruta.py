# 
# Ejercicio 1: Decifrar el mensaje oculto con FUERZA BRUTA 
# 
import re

print ("---Ejercicio uno---\n")

alfabeto = "abcdefghijklmnñopqrstuvwxyz ,."
texto_cifrado = (
    "l.ziu,mf .fzmk,wzilwgfqw mfai kwukmsw flw,wfifsif.upamz plilflmf .fik,.isfm "
    "k.lwfmufmsfk.isfmsfiñ.psiftmcpkiuifdfmsfkwulwzfiulpuwgfk.isfiamfjpkmnisigfxzw,mñmufmsflm "
    "xspmñ.mflmsftixiflmfitmzpkifsi,puigflm lmfsifnzwu,mzifuwz,mflmftmcpkwfoi ,ifmsfkijwflmfowzuw "
    "gfxsi tiulwfsif.upnpkikpwuflmfsw fpjmzwitmzpkiuw gfu.m ,zwfkwu,pumu,mfu.mawfdfiu,pñ.wgfxzmlm ,puilwfifkwu,mumzf.uifzieify.pu,igfsifzieifkw "
    "tpkigfmufsifk.isf mfn.ulpziufsi flp xmz i fdf mfkwu .tizifsif.uplilh"
)

def desplazar_y_descifrar(texto, desplazamiento, abecedario):
    n = len(abecedario)
    # Para descifrar desplazamos cada letra 'desplazamiento' posiciones hacia la izquierda
    mapa = str.maketrans(abecedario, "".join(abecedario[(i - desplazamiento) % n] for i in range(n)))
    return texto.translate(mapa)

def puntuacion_legible(texto):
    palabras = re.findall(r"[a-zñ]+", texto.lower())
    if not palabras:
        return 0, 0
    claves = {"que","la","el","de","y","en","para","con","por","se","no","es","los","las","del","una","al"}
    total = len(palabras)
    coincidencias = sum(1 for w in palabras if w in claves)
    return coincidencias, total

mejor = {"desplazamiento": None, "coincidencias": -1, "total": 0, "texto": None}

for intento in range(len(alfabeto)):
    prueba = desplazar_y_descifrar(texto_cifrado, intento, alfabeto)
    coincidencias, total = puntuacion_legible(prueba)
    if coincidencias > mejor["coincidencias"]:
        mejor.update({"desplazamiento": intento, "coincidencias": coincidencias, "total": total, "texto": prueba})
    ratio = coincidencias / total if total else 0
    if coincidencias >= 20 and ratio >= 0.25:
        print(f"Mensaje encontrado (desplazamiento={intento}):\n")
        print(prueba)
        break
else:
    print("No se detectó ningún descifrado que cumpla el umbral de legibilidad.\n")
    print(f"Mejor candidato (desplazamiento={mejor['desplazamiento']}, coincidencias={mejor['coincidencias']}/{mejor['total']}):\n")
    print(mejor["texto"])

# 
# Ejercicio 2 : Producto mas alto de dos elementos con FUERZA BRUTA
#
print ("\n---Ejercicio 2---")

Elementos = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

productoMayor = None
parMaximo = ()

for i in range(len(Elementos)):
    for j in range(i + 1, len(Elementos)):
        actual = Elementos[i] * Elementos[j]
        if productoMayor is None or actual > productoMayor:
            productoMayor = actual
            parMaximo = (Elementos[i], Elementos[j])

print("\n Resultados del producto \n")
print(f"El par con el producto más alto es {parMaximo}, con un valor de {productoMayor}.")