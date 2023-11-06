import heapq

def prim_spanning_tree():
    num_vertex = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))
    adj = [[] for _ in range(num_vertex)]
    for _ in range(num_edges):
        u, v, w = map(int,input("Enter u,v, weight: ").split())
        adj[u].append((v,w))
        adj[v].append((u,w))

    pq = []
    vis = [False]*num_vertex
    pq.append((0,0))
    total_weight = 0

    while pq:
        wt, node = heapq.heappop(pq)
        if vis[node]:
            continue
        vis[node] = True
        total_weight += wt

        for neighbor, edge_weight in adj[node]:
            if not vis[neighbor]:
                heapq.heappush(pq, (edge_weight, neighbor))
    print("Total cost :", total_weight)

prim_spanning_tree()

