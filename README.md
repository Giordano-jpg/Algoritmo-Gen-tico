# ¿Qué es un Algoritmo Genético (AG)?

<b>Los AG son técnicas de optimización que simulan la evolución natural para resolver problemas.</b> 

En este caso, se basa en generar soluciones iniciales, evaluarlas con una función de aptitud y mejorarlas mediante mutaciones y cruzamientos. El proceso es iterativo y se enfoca en seleccionar las mejores soluciones de cada generación.

# ¿Qué es el Problema del Agente Viajero (TSP):

<b>Es un problema clásico de optimización que consiste en encontrar el recorrido más corto para visitar un conjunto de ciudades y volver al punto de origen sin repetir ciudades.</b> 

En este caso, el problema será resuelto usando un algoritmo genético.

## Método de resolución:

1. **Leer las coordenadas de las ciudades:**
   
   Crear una función para leer un archivo .tsp y almacenar las coordenadas.

2. **Calcular distancias y aptitud:**
   
   Implementar una función para calcular la distancia total de una ruta.
   
   Crear una función que evalúe la aptitud de una ruta: mayor aptitud para rutas más cortas.

4. **Generar población inicial:**

   Crear rutas iniciales aleatorias (padres) que representen posibles soluciones.

5. **Cruzamiento (por ciclos):**

   Implementar un método de cruzamiento para generar hijos a partir de los padres seleccionados.

6. **Mutación:**

   Crear una función que modifique aleatoriamente una ruta (como invertir una subcadena).

7. **Selección por ruleta:**

   Diseñar un mecanismo para seleccionar individuos (rutas) en proporción a su aptitud.

8. **Bucle del algoritmo genético:**

   En cada generación: (por orden de listado)

   - Seleccionar padres.
   - Aplicar cruzamiento y mutación para crear una nueva población.
   - Evaluar la aptitud y repetir el proceso hasta un criterio de parada.

9. **Resultado final:**

   Mostrar la mejor ruta encontrada y su distancia.
