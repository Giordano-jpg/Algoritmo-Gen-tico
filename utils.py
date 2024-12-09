import numpy as np

# Leer el archivo y guardar el ID y las coordenadas en la variable Ciudads
def leer_tsp(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        lines = archivo.readlines()

    # Encontrar la sección NODE_COORD_SECTION
    coords = []
    nodo_seccion = False

    for line in lines:
        line = line.strip()

        if line == "NODE_COORD_SECTION":
            nodo_seccion = True
            continue

        if line == "EOF":
            break

        if nodo_seccion:
            partes = line.split()
            if len(partes) == 3:
                identificador, x, y = partes
                coords.append((int(identificador), float(x), float(y)))

    return coords

# Nombre del archivo con las coordenadas:
ruta = "qa194.tsp"
coordenadas = leer_tsp(ruta) # Leer archivo

# Imprimir lista dentro de "coordenadas"
for ciudad in coordenadas:
    print(ciudad)

# Formula euclidiana (Para calcular la distancia entre dos puntos)
def distancia_euclidiana_np(p1, p2):
    return np.linalg.norm(np.array(p2) - np.array(p1))

# Lista vacía para su posterior uso
distancia_calculada = []

# Calcular la distancia de cada coordenada y guardarla en una lista.
for i in range(len(coordenadas)-1):
    distancia_calculada.append(distancia_euclidiana_np(coordenadas[i], coordenadas[i+1]))

# Imprimir valores calculados
for i in distancia_calculada:
    print(i)

# Obtener el recorrido más óptimo
print("La distancia más corta es:", min(distancia_calculada))
