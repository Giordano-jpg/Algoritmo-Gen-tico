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
def calcular_distancia(p1, p2): # formula euclidiana
    return np.linalg.norm(np.array(p2) - np.array(p1))

# Calcular todas las distancias y guardar los índices de las ciudades
distancias = []
for i in range(len(coordenadas)):
    for j in range(len(coordenadas)):
        distancia = calcular_distancia(coordenadas[i][1:], coordenadas[j][1:])
        distancias.append((distancia, i, j))  # Guardar la distancia y los índices [(distancia, ciudad i, ciudad j)...]

# Crear una lista para almacenar las distancias mayores a 0 porque en la lista se han guardado distancias con ciudades mismas:
distancias_validas = []
for distancia in distancias:
    if distancia[0] > 0:  # Ignorar distancias iguales a 0
        distancias_validas.append(distancia)

# Buscar la distancia mínima:
distancia_mas_corta = distancias_validas[0][0] # primera instancia más corta
ciudad1 = distancias_validas[0][1] # primera ciudad
ciudad2 = distancias_validas[0][2] # segunda ciudad

# iterar sobre las ciudades
for distancia, i, j in distancias_validas:
    if distancia < distancia_mas_corta:
        distancia_mas_corta = distancia # Almacena la distancia más corta/mínima
        ciudad1 = i
        ciudad2 = j

# Mostrar los resultados
print(f"La distancia más corta es: {distancia_mas_corta}")
print(f"Entre la ciudad {ciudad1 + 1} y la ciudad {ciudad2 + 1}")  # +1 para ajustar al identificador original


# FUnción de aptitud
def calcular_aptitud(ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += aptitud(coordenadas[ruta[i] - 1][1:], coordenadas[ruta[i + 1] - 1][1:])
    distancia_total += aptitud(coordenadas[ruta[-1] - 1][1:], coordenadas[ruta[0] - 1][1:])  # Volver al inicio
    return 1 / distancia_total  # Función de aptitud (inverso de la distancia)



# funcion de mutacion para obtener la cadena "hijo"
def generar_padre():
    cantidad_ciudades= len(coordenadas) # cantidad de ciudades
    padre = list(range(1, cantidad_ciudades + 1))  # Crear la lista de ciudades
    random.shuffle(padre)  # Mezclar la lista
    return padre

# guardamos los padres en variables para usarlo más tarde
padre1= generar_padre()
padre2= generar_padre()

# función mutación para usar los hijos
def mutacion(padre):

    tamaño_subcadena= random.randint(2,len(padre)-1) # sacamos un valor aleatorio para una subcadena
    indice_inicio= random.randint(0, len(padre) - tamaño_subcadena) # índice aleatorio de inicio
    subcadena= padre[indice_inicio:indice_inicio + tamaño_subcadena] # con el índice sacamos la subcadena
    subcadena_invertida= subcadena[::-1] # invertir la subcadena
    hijo = padre[:indice_inicio] + subcadena_invertida + padre[indice_inicio + tamaño_subcadena:] # sacamos la cadena final hijo
    #print(subcadena_invertida)
    return hijo # devolver la lista "hijo"

hijo1= mutacion(padre1) # guardar el "hijo" en una variable
hijo2= mutacion(padre2) 

# funcion de técnica de cruzamiento de ciclos
def cruzamiento_ciclos(padre1, padre2):
    hijo1 = [0] * len(padre1)  # Lista vacía para hijo 1
    hijo2 = [0] * len(padre2)  # Lista vacía para hijo 2
    visitados_hijo1 = [False] * len(padre1)  # Lista de booleanos para saber si ya está visitado en hijo1
    visitados_hijo2 = [False] * len(padre2)  # Lista de booleanos para saber si ya está visitado en hijo2

    # Empezamos con el primer elemento del padre1 y padre2
    idx = 0
    while not all(visitados_hijo1) and not all(visitados_hijo2):
        if not visitados_hijo1[idx]:
            # Tomamos el valor de padre1 y lo asignamos a hijo1
            hijo1[idx] = padre1[idx]
            visitados_hijo1[idx] = True

            # Buscamos la posición del valor de padre1 en padre2
            pos_en_padre2 = padre2.index(padre1[idx])

            # Tomamos el valor correspondiente de padre2 y lo asignamos a hijo2
            hijo2[pos_en_padre2] = padre2[pos_en_padre2]
            visitados_hijo2[pos_en_padre2] = True

        # Incrementamos el índice para continuar con el siguiente elemento
        idx += 1

    
    # Ahora rellenamos los espacios vacíos en hijo1 con los valores restantes de padre2
    for i in range(len(hijo1)):
        if hijo1[i] == 0:
            hijo1[i] = padre2[i]

    # Hacemos lo mismo para hijo2, rellenando con los valores restantes de padre1
    for i in range(len(hijo2)):
        if hijo2[i] == 0:
            hijo2[i] = padre1[i]

    
    return hijo1, hijo2 # devolver una tupla con las 2 variables de cada hijo


# si se desea ver el resultado quitar el "#" del print
# print(cruzamiento_ciclos(padre1,padre2))

# Método de selección por ruleta
def seleccion_ruleta(poblacion, aptitudes):
    """
    poblacion: Una lista de individuos (puede ser padres o hijos).
    aptitudes: Una lista de las aptitudes (distancias, en tu caso) de cada individuo.
    Probabilidad: Determina qué tan probable es que cada individuo sea seleccionado.
    """

    total_aptitud = sum(aptitudes)  # Suma de todas las aptitudes
    probabilidad_acumulada = 0      # Inicializar la probabilidad acumulada
    seleccionados = []              # Lista para almacenar individuos seleccionados

    for i in range(len(poblacion)):
        # Probabilidad relativa del individuo
        probabilidad = aptitudes[i] / total_aptitud
        # Acumulamos la probabilidad  
        probabilidad_acumulada += probabilidad        
        
        # Generar un número aleatorio entre 0 y 1
        r = random.random()
        
        # Si el número aleatorio está dentro de la probabilidad acumulada, seleccionamos el individuo
        if r < probabilidad_acumulada:
            seleccionados.append(poblacion[i])  # Añadimos al individuo a la lista de seleccionados
    
    # Devolver los individuos seleccionados
    return seleccionados  



# Crear la población inicial
def crear_poblacion(tamano_poblacion):
    poblacion = []
    for _ in range(tamano_poblacion):
        poblacion.append(generar_padre())  # Rutas aleatorias
    return poblacion

