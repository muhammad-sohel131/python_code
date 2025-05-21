def limited_depth_dfs(graph, current, depth_limit, visited, path):
    if depth_limit < 0:
        return

    visited.add(current)
    path.append(current)

    if depth_limit == 0:
        return

    for neighbor in graph[current]:
        if neighbor not in visited:
            limited_depth_dfs(graph, neighbor, depth_limit - 1, visited, path)

def iterative_deepening_search(graph, source, target, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth {depth}...")
        visited_nodes = set()
        traversal_path = []

        limited_depth_dfs(graph, source, depth, visited_nodes, traversal_path)

        print(f"Visited at depth {depth}: {' -> '.join(traversal_path)}")

        if target in traversal_path:
            print(f"Goal '{target}' found at depth {depth}!")
            return traversal_path

    return None

# Graph definition using node labels
graph_structure = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'P'],
    'D': ['B', 'G', 'I'],
    'E': ['B', 'K'],
    'P': ['C'],
    'I': ['D', 'J', 'K'],
    'G': ['D', 'H'],
    'H': ['G'],
    'J': ['I'],
    'K': ['I', 'E']
}

start = 'A'
goal = 'K'
max_search_depth = 5

final_path = iterative_deepening_search(graph_structure, start, goal, max_search_depth)

if final_path:
    print("\nFinal Path to Goal:")
    print(" -> ".join(final_path))
else:
    print("\nNo path found within the given depth limit.")
