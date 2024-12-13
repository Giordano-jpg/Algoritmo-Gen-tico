# ¿Qué es un Algoritmo Genético (AG)?

<b>Los AG son técnicas de optimización que simulan la evolución natural para resolver problemas.</b> 

En este caso, se basa en generar soluciones iniciales, evaluarlas con una función de aptitud (fitness) y mejorarlas mediante mutaciones y cruzamientos. El proceso es iterativo y se enfoca en seleccionar las mejores soluciones de cada generación.

# ¿Qué es el Problema del Agente Viajero (TSP):

<b>Es un problema clásico de optimización que consiste en encontrar el recorrido más corto para visitar un conjunto de ciudades y volver al punto de origen sin repetir ciudades.</b> 

En este caso, el problema será resuelto usando un algoritmo genético.

## Método de resolución:

1. **Leer las coordenadas de las ciudades:**
   
   Crear una función para leer un archivo .tsp y almacenar las coordenadas en una estructura adecuada ({id, x, y}).

4. **Generar población inicial:**

   Crear rutas iniciales aleatorias (permutaciones de las ciudades/padres) para formar la población inicial.

5. **<ins>Bucle</ins> del algoritmo genético:**

   Iterar los siguientes pasos hasta cumplir el criterio de parada:
   
   Definir los siguientes parámetros:
   
   - Tamaño de la población.
   - Criterio de parada (número máximo de generaciones).

   1. **Calcular distancias y aptitud:**
   
      Implementar una función que calcule las distancias entre dos ciudades usando la fórmula euclidiana.
   
      Dada una ruta completa, calcule su distancia total y el valor de aptitud.

   2. **Selección por ruleta:**
   
      Seleccionar padres basados en la aptitud.

   3. **Cruzamiento (por ciclos):**
   
      Implementar el método de cruzamiento por ciclos para generar hijos válidos a partir de dos rutas padres.

   4. **Mutación (por inversión):**
   
      Reemplazar la población actual con los nuevos individuos generados.

   5. **Crear la nueva población:**
   
      Calcular la distancia total de cada ruta y su aptitud.

   6. **Verificar el criterio de parada:**
   
      Continuar si no se cumple el criterio; detener si se cumple.

8. **Resultado final:**

   Mostrar la mejor ruta encontrada y su distancia.
