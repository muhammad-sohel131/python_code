def dfs(graph, start, depth, visited, result):
    if depth < 0:
        return None
    
    if depth == 0:
        result.append(start)
        return result
    
    visited.add(start)
    result.append(start)

    for neighbor in range(len(graph[start])):
        if(graph[start][neighbor]) == 1 and neighbor not in visited:
            dfs(graph, neighbor, depth - 1, visited, result)
    
    return result

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth):
        print(f"Depth: {depth}")
        visited = set()
        result = []
        print(f"At Depth {depth}: ", end="")

        dfs(graph, start, depth, visited, result)
        print(" ".join(map(str, result)))

        if goal in result:
            print(f"Goal found at depth {depth}: {result}")
            return result
        
    return None

graph = [
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

start_node = 0
goal_node = 6
max_depth = 5

path = iddfs(graph, start_node, goal_node, max_depth)

if not path:
    print("No path found within the maximum depth limit.")