import numpy as np
import random

# Leer el archivo (.tsp) y guardar el ID y las coordenadas en la variable Ciudads
def leer_tsp(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        lines = archivo.readlines()

    # Encontrar la sección NODE_COORD_SECTION del archivo .tsp
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
coordenadas = leer_tsp(ruta)  # Leer archivo

# Imprimir lista dentro de "coordenadas"
for ciudad in coordenadas:
    print(ciudad)

# Fórmula euclidiana (Para calcular la distancia entre dos puntos)
def distancia_euclidiana_np(p1, p2):
    return np.linalg.norm(np.array(p2) - np.array(p1))

# Calcular todas las distancias y guardar los índices de las ciudades
distancias = []
for i in range(len(coordenadas)):
    for j in range(len(coordenadas)):
        distancia = distancia_euclidiana_np(coordenadas[i][1:], coordenadas[j][1:])
        distancias.append((distancia, i, j))  # Guardar la distancia y los índices

# Crear una lista para almacenar las distancias mayores a 0 porque en la lista se han guardado distancias con ciudades mismas
distancias_validas = []
for distancia in distancias:
    if distancia[0] > 0:  # Ignorar distancias iguales a 0
        distancias_validas.append(distancia)

# Buscar la distancia mínima
distancia_mas_corta = distancias_validas[0][0] # primera instancia más corta
ciudad1 = distancias_validas[0][1] # primera ciudad
ciudad2 = distancias_validas[0][2] # segunda ciudad

# iterar sobre las ciudades
for distancia, i, j in distancias_validas:
    if distancia < distancia_mas_corta:
        distancia_mas_corta = distancia
        ciudad1 = i
        ciudad2 = j

# Mostrar los resultados
print(f"La distancia más corta es: {distancia_mas_corta}")
print(f"Entre la ciudad {ciudad1 + 1} y la ciudad {ciudad2 + 1}")  # +1 para ajustar al identificador original


# funcion de mutacion para obtener la cadena "hijo"
def mutacion():
    cantidad_ciudades= len(coordenadas) # cantidad de ciudades
    padre= list(random.shuffle(range(1,cantidad_ciudades+1))) # lista de números del 1 al 194, que despues se mezclan los números

    tamaño_subcadena= random.randint(2,len(padre)-1) # sacamos un valor aleatorio para una subcadena
    indice_inicio= random.randint(0, len(padre) - tamaño_subcadena) # índice aleatorio de inicio
    subcadena= padre[indice_inicio:indice_inicio + tamaño_subcadena] # con el índice sacamos la subcadena
    subcadena_invertida= subcadena[::-1] # invertir la subcadena
    hijo = padre[:indice_inicio] + subcadena_invertida + padre[indice_inicio + tamaño_subcadena:] # sacamos la cadena final hijo
    #print(subcadena_invertida)
    return hijo # devolver la lista "hijo"

hijo= mutacion() # guardar el "hijo" en una variable
#print(hijo) # imprimir la cadena si se quiere visualizar


