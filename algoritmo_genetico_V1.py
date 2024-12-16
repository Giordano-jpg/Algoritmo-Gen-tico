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




# Calcular la distancia total de una ruta
def calcular_distancia_total(ruta, coordenadas):
   distancia_total = 0
   for i in range(len(ruta) - 1):
       distancia_total += calcular_distancia(coordenadas[ruta[i] - 1][1:], coordenadas[ruta[i + 1] - 1][1:])
   distancia_total += calcular_distancia(coordenadas[ruta[-1] - 1][1:], coordenadas[ruta[0] - 1][1:])  # Volver al inicio
   return distancia_total


"""# Obtener la ruta más corta:


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


"""


# Función de aptitud
def calcular_aptitud(ruta, coordenadas):
   distancia_total = calcular_distancia_total(ruta, coordenadas)
   return 1 / distancia_total  # Aptitud: inverso de la distancia




# Crear un individuo (ruta aleatoria)
def generar_padre(cantidad_ciudades):
   padre = list(range(1, cantidad_ciudades + 1))  # Crear la lista de ciudades
   random.shuffle(padre)  # Mezclar la lista
   return padre


""""
# funcion de mutacion para obtener la cadena "hijo"
def generar_padre():
   cantidad_ciudades= len(coordenadas) # cantidad de ciudades
   padre = list(range(1, cantidad_ciudades + 1))  # Crear la lista de ciudades
   random.shuffle(padre)  # Mezclar la lista
   return padre
"""
# Crear la población inicial
def crear_poblacion(tamano_poblacion, cantidad_ciudades):
   return [generar_padre(cantidad_ciudades) for _ in range(tamano_poblacion)]


# Generar población inicial
cantidad_ciudades = len(coordenadas)
poblacion_inicial = crear_poblacion(10, cantidad_ciudades)  # Población de 10 rutas


# Evaluar la distancia total de cada ruta
for i, ruta in enumerate(poblacion_inicial):
   distancia = calcular_distancia_total(ruta, coordenadas)
   aptitud = calcular_aptitud(ruta, coordenadas)
   print(f"Ruta {i + 1}: {ruta} - Distancia total: {distancia:.2f} - Aptitud: {aptitud:.6f}")






""""
# guardamos los padres en variables para usarlo más tarde
padre1= generar_padre()
padre2= generar_padre()
"""


# función mutación para usar los hijos
def mutacion(padre):


   tamaño_subcadena= random.randint(2,len(padre)-1) # sacamos un valor aleatorio para una subcadena
   indice_inicio= random.randint(0, len(padre) - tamaño_subcadena) # índice aleatorio de inicio
   subcadena= padre[indice_inicio:indice_inicio + tamaño_subcadena] # con el índice sacamos la subcadena
   subcadena_invertida= subcadena[::-1] # invertir la subcadena
   hijo = padre[:indice_inicio] + subcadena_invertida + padre[indice_inicio + tamaño_subcadena:] # sacamos la cadena final hijo
   #print(subcadena_invertida)
   return hijo # devolver la lista "hijo"


#hijo1= mutacion(padre1) # guardar el "hijo" en una variable
#hijo2= mutacion(padre2)


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
def seleccion_ruleta(poblacion, coordenadas):
   # Calcular aptitudes
   aptitudes = [calcular_aptitud(ruta, coordenadas) for ruta in poblacion]
  
   # Calcular probabilidades de selección
   suma_aptitudes = sum(aptitudes)
   probabilidades = [apt / suma_aptitudes for apt in aptitudes]
  
   # Calcular probabilidades acumuladas
   probabilidades_acumuladas = np.cumsum(probabilidades)
  
   # Seleccionar individuos
   nueva_poblacion = []
   for _ in range(len(poblacion)):  # Selecciona tantos individuos como el tamaño de la población
       r = random.random()
       for i, prob_acum in enumerate(probabilidades_acumuladas):
           if r <= prob_acum:
               nueva_poblacion.append(poblacion[i])
               break
  
   return nueva_poblacion


# Selección por ruleta
poblacion_seleccionada = seleccion_ruleta(poblacion_inicial, coordenadas)


# Ver los resultados de la selección
for i, ruta in enumerate(poblacion_seleccionada):
   distancia = calcular_distancia_total(ruta, coordenadas)
   aptitud = calcular_aptitud(ruta, coordenadas)
   print(f"Ruta seleccionada {i + 1}: {ruta} - Distancia total: {distancia:.2f} - Aptitud: {aptitud:.6f}")




# Función para aplicar el cruzamiento por ciclo (PMX)
def pmx_crossover(parent1, parent2):
   length = len(parent1)
  
   # Randomly select start and end points for the cycle
   start, end = sorted(random.sample(range(length), 2))
  
   # Create offspring using partially matched crossover
   offspring = [-1] * length
   for i in range(start, end):
       offspring[i] = parent1[i]
  
   for i in range(start, end):
       if parent2[i] not in offspring[start:end]:
           for j in range(length):
               if offspring[j] == -1:
                   offspring[j] = parent2[i]
                   break
  
   for i in range(length):
       if offspring[i] == -1:
           for j in range(length):
               if parent2[j] not in offspring:
                   offspring[i] = parent2[j]
                   break
  
   return offspring




# Ejemplo de padres
parent1 = [0, 1, 2, 3, 4, 5, 6]
parent2 = [0, 2, 4, 6, 1, 3, 5]


# Aplicamos el cruce
offspring = pmx_crossover(parent1, parent2)
print("Padre 1:", parent1)
print("Padre 2:", parent2)
print("Hijo:", offspring)




# Función para aplicar la mutación
def mutation(individual, mutation_rate=0.01):
   length = len(individual)
   mutated = individual[:]
   for i in range(length):
       if random.random() < mutation_rate:
           # Selecciona una posición aleatoria para mutar
           swap_index = random.randint(0, length - 1)
           # Intercambia el valor de las dos posiciones
           mutated[i], mutated[swap_index] = mutated[swap_index], mutated[i]
   return mutated


# Ejemplo de hijo
offspring = [0, 1, 3, 5, 2, 4, 6]


# Aplicamos la mutación
mutated_offspring = mutation(offspring, mutation_rate=0.05)
print("Hijo original:", offspring)
print("Hijo mutado:", mutated_offspring)




# Función para generar la nueva población por cruce y mutación
def evolucionar(poblacion, coordenadas, tasa_mutacion=0.01):
   nueva_poblacion = []
  
   # Selección por ruleta
   poblacion_seleccionada = seleccion_ruleta(poblacion, coordenadas)
  
   # Cruzamiento (Crossover por ciclos o PMX)
   for i in range(0, len(poblacion_seleccionada), 2):
       padre1 = poblacion_seleccionada[i]
       padre2 = poblacion_seleccionada[i + 1]
      
       # Cruzamiento por ciclos o PMX
       hijo1 = pmx_crossover(padre1, padre2)  # Ajustado para manejar el resultado único
       hijo2 = pmx_crossover(padre2, padre1)  # Cruzamiento en orden inverso
      
       # Aplicar mutación
       hijo1 = mutation(hijo1, tasa_mutacion)
       hijo2 = mutation(hijo2, tasa_mutacion)
      
       nueva_poblacion.extend([hijo1, hijo2])
  
   return nueva_poblacion




# Función para ejecutar el algoritmo genético
def ejecutar_algoritmo(coordenadas, tamano_poblacion, generaciones, tasa_mutacion):
   poblacion = crear_poblacion(tamano_poblacion, len(coordenadas))
  
   for generacion in range(generaciones):
       poblacion = evolucionar(poblacion, coordenadas, tasa_mutacion)
      
       # Evaluar y mostrar resultados
       mejores_rutas = []
       for ruta in poblacion:
           distancia = calcular_distancia_total(ruta, coordenadas)
           aptitud = calcular_aptitud(ruta, coordenadas)
           mejores_rutas.append((distancia, aptitud, ruta))
      
       mejores_rutas.sort(key=lambda x: x[1], reverse=True)  # Ordenar por aptitud
       mejor_ruta = mejores_rutas[0]
      
       print(f"Generación {generacion + 1}: Mejor Distancia = {mejor_ruta[0]:.2f}, Aptitud = {mejor_ruta[1]:.6f}")
  
   mejor_distancia = mejores_rutas[0][0]
   mejor_ruta = mejores_rutas[0][2]
  
   print("Mejor ruta final:", mejor_ruta)
   print("Distancia final más corta:", mejor_distancia)




# Ejecutamos el algoritmo
ejecutar_algoritmo(coordenadas, tamano_poblacion=10, generaciones=100, tasa_mutacion=0.05)


