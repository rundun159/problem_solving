import  heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = []
    heapq.heappush(heap, [distances[start],start])
    while heap:
        now_dist, now_node = heapq.heappop(heap)
        print(distances[now_node], now_dist)
        if distances[now_node] < now_dist:
            continue
        # distances[now_node] = now_dist
        for next_node, edge in graph[now_node].items():
            new_dist = now_dist + edge
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(heap, [new_dist, next_node])
    return distances
print(dijkstra(graph,'A'))

# print(distances)
# for node,item in graph.items():
#     print(node,item)