# Documentación - Algoritmo de Dijkstra

## 📋 Contenido
1. [Explicación General](#explicación-general)
2. [Funcionamiento del Código](#funcionamiento-del-código)
3. [Glosario de Funciones](#glosario-de-funciones)
4. [Cómo Usar](#cómo-usar)

---

## Explicación General

El **Algoritmo de Dijkstra** es un algoritmo de búsqueda de caminos que encuentra la ruta más corta desde un nodo origen hacia todos los demás nodos en un grafo con pesos positivos.

### ¿Para qué sirve?
- Encontrar la distancia mínima entre estaciones de transporte
- Calcular rutas óptimas en sistemas de navegación GPS
- Determinar el camino más eficiente en redes de comunicación
- Resolver problemas de optimización de rutas

### Características
- ✅ Encuentra caminos mínimos globales (óptimos)
- ✅ Funciona con grafos ponderados
- ✅ Eficiente con cola de prioridad (heap)
- ✅ Complejidad O((V + E) log V)

---

## Funcionamiento del Código

### Paso a Paso

#### 1. **Inicialización**
```python
dist = {node: float('inf') for node in graph}  # Distancias infinitas
dist[start] = 0  # Nodo inicial con distancia 0
parent = {node: None for node in graph}  # Rastrear padres
pq = [(0, start)]  # Cola de prioridad
```
Se inicializan las distancias a infinito (inalcanzables), excepto el nodo inicial que es 0.

#### 2. **Exploración de Nodos**
```python
while pq:
    current_dist, current_node = heapq.heappop(pq)
```
Se extrae el nodo con la menor distancia de la cola de prioridad.

#### 3. **Relajación de Aristas**
```python
for neighbor in graph[current_node]:
    weight = graph[current_node][neighbor]
    distance = current_dist + weight
    
    if distance < dist[neighbor]:
        dist[neighbor] = distance
        parent[neighbor] = current_node
        heapq.heappush(pq, (distance, neighbor))
```
Se verifica si hay un camino más corto hacia cada vecino. Si lo hay, se actualiza.

#### 4. **Reconstrucción de Caminos**
```python
for node in graph:
    path = []
    current = node
    while current is not None:
        path.append(current)
        current = parent[current]
    paths[node] = path[::-1]
```
Se reconstruyen los caminos completos usando el diccionario de padres.

### Ejemplo Visual

Para el grafo:
```
A → B (peso 5)
A → C (peso 10)
B → C (peso 3)
B → E (peso 7)
C → D (peso 1)
D → E (peso 2)
```

Desde A:
- A → A: distancia = 0, camino = [A]
- A → B: distancia = 5, camino = [A, B]
- A → C: distancia = 8, camino = [A, B, C]
- A → D: distancia = 9, camino = [A, B, C, D]
- A → E: distancia = 11, camino = [A, B, C, D, E]

---

## Glosario de Funciones

### 🔹 `dijkstra(graph, start)`

**Descripción:** Principal función que implementa el algoritmo de Dijkstra.

**Parámetros:**
- `graph` (dict): Grafo representado como diccionario de diccionarios
  - Formato: `{nodo: {vecino: peso, ...}}`
  - Ejemplo: `{'A': {'B': 5, 'C': 10}, 'B': {'C': 3}}`
- `start` (str): Nodo de inicio (estación de origen)

**Retorna:**
- `tuple`: Una tupla con dos diccionarios:
  - `dist` (dict): Distancia mínima desde `start` a cada nodo
  - `paths` (dict): Camino mínimo (lista de nodos) desde `start` a cada nodo

**Ejemplo de uso:**
```python
grafo = {
    'A': {'B': 5, 'C': 10},
    'B': {'C': 3, 'E': 7},
    'C': {'D': 1},
    'D': {'E': 2},
    'E': {}
}
dist, paths = dijkstra(grafo, 'A')
print(dist)   # {'A': 0, 'B': 5, 'C': 8, 'D': 9, 'E': 11}
print(paths)  # {'A': ['A'], 'B': ['A', 'B'], ...}
```

---

### 🔹 `mostrar_resultados(start, distancias, caminos)`

**Descripción:** Función auxiliar que imprime los resultados de forma legible y formateada.

**Parámetros:**
- `start` (str): Estación de origen
- `distancias` (dict): Diccionario de distancias (retornado por `dijkstra()`)
- `caminos` (dict): Diccionario de caminos (retornado por `dijkstra()`)

**Retorna:** `None` (solo imprime en consola)

**Ejemplo de salida:**
```
============================================================
Caminos mínimos desde la estación A
============================================================

A: Estación de inicio

B: Distancia = 5
     Camino: A → B

C: Distancia = 8
     Camino: A → B → C

D: Distancia = 9
     Camino: A → B → C → D

E: Distancia = 11
     Camino: A → B → C → D → E
```

---

## 📚 Módulos y Librerías Usadas

### `heapq`
Módulo de Python para gestionar colas de prioridad (min-heap).

**Funciones principales:**
- `heapq.heappop(heap)`: Extrae y retorna el elemento con menor prioridad
- `heapq.heappush(heap, item)`: Inserta un elemento manteniendo la estructura heap

**¿Por qué se usa?** Permite obtener eficientemente el nodo con menor distancia sin revisar todos los nodos.

---

## Cómo Usar

### Opción 1: Usar las funciones directamente

```python
from Grafo import dijkstra, mostrar_resultados

# Definir tu grafo
mi_grafo = {
    'A': {'B': 5, 'C': 10},
    'B': {'C': 3, 'E': 7},
    'C': {'D': 1},
    'D': {'E': 2},
    'E': {}
}

# Calcular caminos desde A
dist, paths = dijkstra(mi_grafo, 'A')

# Mostrar resultados
mostrar_resultados('A', dist, paths)
```

### Opción 2: Ejecutar el archivo completo

```bash
python Grafo.py
```

Esto calculará automáticamente los caminos mínimos desde TODAS las estaciones (A, B, C, D, E).

---

## 🎯 Casos de Uso Prácticos

| Caso | Descripción |
|------|-------------|
| **Navegación GPS** | Encontrar la ruta más corta entre dos ciudades |
| **Redes de datos** | Enrutar paquetes por el camino más eficiente |
| **Transporte público** | Calcular la conexión más rápida entre estaciones |
| **Videojuegos** | Movimiento de personajes en mapas |
| **Redes sociales** | Grados de separación entre usuarios |

---

## ⚠️ Limitaciones

- ❌ No funciona con pesos negativos (usar Bellman-Ford en ese caso)
- ❌ No funciona en grafos desconectados (algunos nodos serán inalcanzables)
- ❌ Requiere que el grafo esté completamente definido en memoria

---

## 📝 Notas Importantes

1. **El grafo debe ser un diccionario de diccionarios**: Cada nodo apunta a un diccionario con sus vecinos y pesos
2. **Todos los nodos deben estar en el diccionario principal**: Incluso si no tienen vecinos, deben tener un diccionario vacío
3. **Los pesos deben ser positivos**: El algoritmo de Dijkstra no funciona correctamente con pesos negativos
4. **El resultado incluye el nodo inicial**: La distancia de A a A es siempre 0

---

**Última actualización:** Marzo 2026
**Autor:** Documentación del Algoritmo de Dijkstra
