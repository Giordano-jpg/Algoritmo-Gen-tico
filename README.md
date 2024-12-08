# ¿Qué es un Algoritmo Genético (AG)?

<b>Los AG son técnicas de optimización que simulan la evolución natural para resolver problemas.</b> En ste caso, se basa en generar soluciones iniciales (cromosomas), evaluarlas con una función de aptitud (fitness) y mejorarlas mediante mutaciones y cruzamientos. El proceso es iterativo y se enfoca en seleccionar las mejores soluciones de cada generación.

# ¿Qué es el Problema del Agente Viajero (TSP):

<b>Es un problema clásico de optimización que consiste en encontrar el recorrido más corto para visitar un conjunto de ciudades y volver al punto de origen sin repetir ciudades.</b> En este caso, el problema será resuelto usando un algoritmo genético, donde:
* Los cromosomas representan los recorridos de las ciudades.
* La función de aptitud evalúa la distancia total de cada recorrido.

# Componentes principales del algoritmo genético:

* <b>Cromosomas:</b> Se representan como cadenas de números enteros, donde cada número es una ciudad.
* <b>Función de aptitud:</b> Calcula la distancia total entre ciudades usando la fórmula de distancia euclidiana.
* <b>Mutación por inversión:</b> Invierte una subcadena aleatoria dentro del cromosoma.
* <b>Cruzamiento por ciclos:</b> Combina dos cromosomas (padres) para generar nuevos cromosomas (hijos).
* <b>Métodos de selección:</b>
    * <b>Ruleta:</b> Selecciona individuos proporcionalmente a su aptitud.
    * <b>Torneo:</b> Compara aleatoriamente dos individuos y elige al mejor.

