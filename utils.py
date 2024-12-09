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
                _, x, y = partes  # Ignorar el índice
                coords.append((float(x), float(y)))

    return coords

# Ejemplo de uso
ruta = "qa194.tsp"
coordenadas = leer_tsp(ruta)
