# class Graph:
#     def __init__(self, num_vertices):
#         self.num_vertices = num_vertices
#         self.edges = [[] for _ in range(num_vertices)]

#     def add_edge(self, start, end):
#         self.edges[start].append(end)
#         self.edges[end].append(start)

# def graph_coloring_backtracking(graph):
#     def is_valid_coloring(coloring, vertex, color):
#         return all(coloring[neighbor] != color for neighbor in graph.edges[vertex])

#     def backtrack_coloring(current_vertex):
#         if current_vertex == graph.num_vertices:
#             return True  # All vertices colored

#         for color in range(1, max_colors + 1):
#             if is_valid_coloring(coloring, current_vertex, color):
#                 coloring[current_vertex] = color

#                 if backtrack_coloring(current_vertex + 1):
#                     return True  # Move to the next vertex

#         return False

#     max_colors = graph.num_vertices
#     coloring = [0] * graph.num_vertices

#     return coloring if backtrack_coloring(0) else None

# # Take user input to define the graph
# graph = Graph(int(input("Enter the number of vertices: ")))

# num_edges = int(input("Enter the number of edges: "))
# for _ in range(num_edges):
#     start, end = map(int, input("Enter edge (start end): ").split())
#     graph.add_edge(start, end)

# # Solve the graph coloring problem using backtracking
# coloring = graph_coloring_backtracking(graph)

# if coloring:
#     print("Valid Coloring:", coloring)
# else:
#     print("No valid coloring exists.")

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = [[]for _ in range(num_vertices)]

    def add_edge(self, start, end):
        self.edges[start].append(end)
        self.edges[end].append(start)

def graph_coloring(graph):
    max_colors = graph.num_vertices
    coloring = [0]* graph.num_vertices
    def valid_coloring(coloring, vertex, color):
        return all(coloring[neighbor] != color for neighbor in graph.edges[vertex])
    
    def backtracking(current_vertex):
        if current_vertex == graph.num_vertices:
            return True
        for color in range(1, max_colors + 1):
            if valid_coloring(coloring, current_vertex, color):
                coloring[current_vertex] = color
                if backtracking(current_vertex + 1):
                    return True
        return False
    
    return coloring if backtracking(0) else None

graph = Graph(int(input("Enter number of vertices: ")))
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):
    start, end = map(int,input("Enter start and end: ").split())
    graph.add_edge(start, end)

coloring = graph_coloring(graph)
if coloring:
    print("Valid: ",coloring)
else:
    print("Invalid")