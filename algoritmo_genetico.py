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

# Calcular todas las distancias
distancias = []
for i in range(len(coordenadas)):
    for j in range(len(coordenadas)):
        distancias.append(distancia_euclidiana_np(coordenadas[i], coordenadas[j]))

# Validar que se calculen 194 x 194 distancias
print("Número total de distancias calculadas:", len(distancias))  # Esto debería ser 194 * 194 = 37636


# Crear una lista para almacenar las distancias mayores a 0
distancias_validas = []
for distancia in distancias:
    # Ignorar la distancia a sí mismo (0.0)
    if distancia > 0: 
        distancias_validas.append(distancia)

# Calcular la distancia más corta de las distancias válidas
distancia_mas_corta = min(distancias_validas)
print("La distancia más corta es:", distancia_mas_corta)