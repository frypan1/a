import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {}

num_vertices = int(input("Enter the number of vertices: "))

for i in range(num_vertices):
    num_edges = int(input(f"Enter the number of edges connected to vertex {i}: "))
    edges = input(f"Enter the edges (vertex weight, vertex weight): ")
    edges = [int(val) for val in edges.split()]
    if len(edges) != num_edges * 2:
        print(f"Error: Expected {num_edges} edges, but received {len(edges) // 2}.")
        exit(1)
    graph[i] = [(edges[j], edges[j + 1]) for j in range(0, len(edges), 2)]

start_vertex = int(input("Enter the starting vertex: "))

result = dijkstra(graph, start_vertex)
print(result)

