import heapq

def astar(start, goal, graph, h):
    if start not in graph or goal not in graph:
        return []

    pq = []
    heapq.heappush(pq, (h.get(start, 0), 0, start, [start]))
    paths = []

    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal:
            paths.append((path, g))
            continue

        for neighbor, cost in graph.get(current, []):
            if neighbor not in path:
                g2 = g + cost
                f2 = g2 + h.get(neighbor, float('inf'))
                heapq.heappush(pq, (f2, g2, neighbor, path + [neighbor]))

    return paths


graph = {
    'A': [('B',2), ('C', 6)],
    'B': [('A', 2), ('D', 4), ('E', 2)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 4), ('G', 2)],
    'E': [('B', 2), ('H', 4), ('G', 3)],
    'F': [('C', 2), ('H', 3)],
    'G': [('D', 2), ('E', 3), ('I', 2)],
    'H': [('F', 3), ('E', 4), ('I', 2)],
    'I': [('H', 2), ('G', 2), ('J', 1)],
    'J': [('I', 1)]
}

h = {
    'A': 7,
    'B': 6,
    'C': 6,
    'D': 5,
    'E': 4,
    'F': 5,
    'G': 3,
    'H': 2,
    'I': 1,
    'J': 0
}

start = 'A'
goal = 'J'

paths = astar(start, goal, graph, h)

# Print all paths
i = 0
print(f"All possible paths from {start} to {goal}:")
for (path, cost) in paths:
    i = i + 1
    print(f"Path {i}: {path}, Cost: {cost}")

optimal_path, optimal_cost = paths[0]
for path, cost in paths[1:]:
    if cost < optimal_cost:
        optimal_path, optimal_cost = path, cost
print(f"\nOptimal Path: {optimal_path}\nTotal Cost: {optimal_cost}")
