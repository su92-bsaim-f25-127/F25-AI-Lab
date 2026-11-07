import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}


def search(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded = []

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if cost != best[node]:
            continue

        if node == goal:
            return path, cost, expanded

        expanded.append(node)

        for nxt, w in graph[node]:
            new_cost = cost + w

            if new_cost < best.get(nxt, float("inf")):
                best[nxt] = new_cost
                heapq.heappush(
                    pq, (new_cost + h[nxt], new_cost,
                         nxt, path + [nxt])
                )

    return None, float("inf"), expanded


# Task 1: A* Search
print("TASK 1: A* SEARCH")
path, cost, nodes = search(graph, h, "S", "G")

print("Path:", path)
print("Cost:", cost)
print("Expanded Nodes:", nodes)
print("Expansion Count:", len(nodes))


# Task 2: A* and UCS Comparison
print("\nTASK 2: A* AND UCS")

zero_h = {n: 0 for n in graph}
ucs_path, ucs_cost, ucs_nodes = search(
    graph, zero_h, "S", "G"
)

print("UCS Path:", ucs_path)
print("UCS Cost:", ucs_cost)
print("UCS Expanded:", ucs_nodes)
print("UCS Count:", len(ucs_nodes))


# Task 3: Change Heuristic of C
print("\nTASK 3: HEURISTIC MODIFICATION")

new_h = h.copy()
new_h["C"] = 10

new_path, new_cost, new_nodes = search(
    graph, new_h, "S", "G"
)

print("Modified Path:", new_path)
print("Modified Cost:", new_cost)
print("Expanded Nodes:", new_nodes)
print("Expansion Count:", len(new_nodes))


# Heuristic Audit
print("\nHEURISTIC AUDIT")

for n in graph:
    print(n, "=", h[n])

print("Original C:", h["C"])
print("Modified C:", new_h["C"])