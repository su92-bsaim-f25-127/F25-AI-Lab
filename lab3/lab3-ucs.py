import heapq

weighted_graph = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 2), ("E", 1)],
    "C": [("F", 2), ("G", 7)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}

# Uniform Cost Search
def ucs(start, goal):
    pq = [(0, start, [start])]
    seen = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node in seen:
            continue

        seen.add(node)

        for n, weight in weighted_graph[node]:
            if n not in seen:
                heapq.heappush(
                    pq, (cost + weight, n, path + [n])
                )


print("UCS Path and Cost:", ucs("A", "G"))