graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

# Depth Limited Search
def dls(start, goal, limit):
    stack = [(start, [start], 0)]

    while stack:
        node, path, depth = stack.pop()

        if node == goal:
            return path

        if depth == limit:
            continue

        for n in reversed(graph[node]):
            if n not in path:
                stack.append((n, path + [n], depth + 1))

    return "Cutoff"


# Iterative Deepening DFS
def iddfs(start, goal, max_depth):
    for limit in range(max_depth + 1):
        result = dls(start, goal, limit)
        print("Depth", limit, ":", result)

        if result != "Cutoff":
            return result


print("DLS:")
for limit in range(1, 5):
    print("Limit", limit, ":", dls("A", "G", limit))

print("\nIDDFS:")
print("Final Path:", iddfs("A", "G", 4))