from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

# Breadth First Search
def bfs(start, goal):
    q = deque([(start, [start])])
    seen = {start}

    while q:
        node, path = q.popleft()

        if node == goal:
            return path

        for n in graph[node]:
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))


# Depth First Search
def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node in seen:
            continue

        seen.add(node)

        for n in reversed(graph[node]):
            stack.append((n, path + [n]))


print("BFS:", bfs("A", "G"))
print("DFS:", dfs("A", "G"))