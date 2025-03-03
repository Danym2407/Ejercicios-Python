import heapq

def dijkstra(graph, start):
    # Diccionario de distancias inicializado con infinito
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Cola de prioridad con el nodo de inicio
    pq = [(0, start)]  # (distancia, nodo)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue  # Si ya encontramos un camino más corto, ignoramos
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Representación de los grafos como diccionarios de adyacencia

graph_IV = {
    1: {2: 3, 3: 1},
    2: {4: 3},
    3: {2: 1, 5: 2},
    4: {},
    5: {7: 3},
    7: {6: 1},
    6: {}
}

graph_V = {
    1: {2: 1, 5: 4},
    2: {3: 3},
    3: {4: 2},
    4: {},
    5: {3: 5, 6: 7},
    6: {}
}

graph_VII = {
    'A': {'B': 9, 'C': 2},
    'B': {},
    'C': {'D': 3, 'E': 6},
    'D': {},
    'E': {'F': 3},
    'F': {}
}

# Pruebas con los grafos
print("Distancias desde el nodo 1 en el grafo IV:", dijkstra(graph_IV, 1))
print("Distancias desde el nodo 1 en el grafo V:", dijkstra(graph_V, 1))
print("Distancias desde el nodo A en el grafo VII:", dijkstra(graph_VII, 'A'))
