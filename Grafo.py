import heapq

def dijkstra(graph, start):
    """
    Calcula los caminos mínimos desde una estación a todas las demás.
    """
    # Inicializar distancias y caminos
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    parent = {node: None for node in graph}
    pq = [(0, start)]  # (distancia, nodo)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Si encontramos una distancia mayor, la ignoramos
        if current_dist > dist[current_node]:
            continue

        # Revisar todos los vecinos
        for neighbor in graph[current_node]:
            weight = graph[current_node][neighbor]
            distance = current_dist + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                parent[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruir los caminos
    paths = {}
    for node in graph:
        if dist[node] == float('inf'):
            paths[node] = None  # Nodo inalcanzable
        else:
            path = []
            current = node
            while current is not None:
                path.append(current)
                current = parent[current]
            paths[node] = path[::-1]  # Invertir para obtener el orden correcto

    return dist, paths


def mostrar_resultados(start, distancias, caminos):
    """
    Muestra los resultados de forma legible.
    """
    print(f"\n{'='*60}")
    print(f"Caminos mínimos desde la estación {start}")
    print('='*60)
    
    for nodo in sorted(distancias.keys()):
        if nodo == start:
            print(f"\n{start}: Estación de inicio")
        elif distancias[nodo] == float('inf'):
            print(f"\n{nodo}: Inalcanzable")
        else:
            camino_str = " → ".join(caminos[nodo])
            print(f"\n{nodo}: Distancia = {distancias[nodo]}")
            print(f"     Camino: {camino_str}")


# Definir el grafo
grafo = {
    'A': {'B': 5, 'C': 10},
    'B': {'C': 3, 'E': 7},
    'C': {'D': 1},
    'D': {'E': 2},
    'E': {}
}

# Pruebas con diferentes estaciones
if __name__ == "__main__":
    estaciones = ['A', 'B', 'C', 'D', 'E']
    
    for estacion in estaciones:
        dist, paths = dijkstra(grafo, estacion)
        mostrar_resultados(estacion, dist, paths)