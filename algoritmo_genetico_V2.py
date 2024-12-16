import random
import math

# Paso 1: Leer el archivo .tsp
def leer_tsp(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()

    coordenadas = []
    comenzar_lectura = False
    for linea in lineas:
        if "NODE_COORD_SECTION" in linea:
            comenzar_lectura = True
            continue
        if "EOF" in linea or linea.strip() == "":
            break
        if comenzar_lectura:
            _, x, y = linea.strip().split()
            coordenadas.append((float(x), float(y)))

    return coordenadas

# Paso 2: Función de distancia
def distancia(ciudad1, ciudad2):
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calcular_distancia_total(ruta, coordenadas):
    distancia_total = 0
    for i in range(len(ruta)):
        ciudad_actual = coordenadas[ruta[i]]
        ciudad_siguiente = coordenadas[ruta[(i + 1) % len(ruta)]]
        distancia_total += distancia(ciudad_actual, ciudad_siguiente)
    return distancia_total

# Paso 3: Algoritmo Genético
def generar_poblacion_inicial(coordenadas, tamaño_población):
    num_ciudades = len(coordenadas)
    return [random.sample(range(num_ciudades), num_ciudades) for _ in range(tamaño_población)]

def seleccionar_padres(población, coordenadas):
    # Selección por ruleta
    aptitudes = [1 / calcular_distancia_total(ruta, coordenadas) for ruta in población]
    total_aptitud = sum(aptitudes)
    probabilidades = [aptitud / total_aptitud for aptitud in aptitudes]
    padres = random.choices(población, weights=probabilidades, k=2)
    return padres

def cruzamiento_ciclo(padre1, padre2):
    hijo = [-1] * len(padre1)
    inicio = 0
    while -1 in hijo:
        ciclo = set()
        idx = inicio
        while idx not in ciclo:
            ciclo.add(idx)
            hijo[idx] = padre1[idx]
            idx = padre1.index(padre2[idx])
        inicio = hijo.index(-1) if -1 in hijo else -1
    return hijo

def mutar(ruta, prob_mutacion):
    if random.random() < prob_mutacion:
        i, j = random.sample(range(len(ruta)), 2)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

def algoritmo_genetico(coordenadas, generaciones, tamaño_población, prob_mutacion):
    # Inicializar población
    población = generar_poblacion_inicial(coordenadas, tamaño_población)
    
    for _ in range(generaciones):
        nueva_generación = []
        for _ in range(tamaño_población):
            padre1, padre2 = seleccionar_padres(población, coordenadas)
            hijo = cruzamiento_ciclo(padre1, padre2)
            hijo = mutar(hijo, prob_mutacion)
            nueva_generación.append(hijo)
        población = nueva_generación

    # Encontrar la mejor solución
    mejor_ruta = min(población, key=lambda ruta: calcular_distancia_total(ruta, coordenadas))
    mejor_distancia = calcular_distancia_total(mejor_ruta, coordenadas)
    return mejor_ruta, mejor_distancia

# Paso 4: Ejecutar el algoritmo
ruta = "qa194.tsp"
coordenadas = leer_tsp(ruta)
mejor_ruta, mejor_distancia = algoritmo_genetico(
    coordenadas, generaciones=100, tamaño_población=30, prob_mutacion=0.05
)

print(f"Mejor ruta: {mejor_ruta}")
print(f"Distancia más corta: {mejor_distancia}")
