from collections import deque

def find_adjacent(r, c, max_row, max_col):
    adjacent = []
    if r + 1 < max_row:
        adjacent.append((r + 1, c))
    if c + 1 < max_col:
        adjacent.append((r, c + 1))
    return adjacent

def robot_topo_sort(row_count, col_count):
    adjacency_list = {}
    incoming_edges = {}

    for r in range(row_count):
        for c in range(col_count):
            cell = (r, c)
            adjacency_list[cell] = []
            incoming_edges[cell] = 0
  
  
    for r in range(row_count):
        for c in range(col_count):
            current = (r, c)
            for neighbor in find_adjacent(r, c, row_count, col_count):
                adjacency_list[current].append(neighbor)
                incoming_edges[neighbor] += 1

    zero_indegree = deque()
    for node in incoming_edges:
        if incoming_edges[node] == 0:
            zero_indegree.append(node)

    topo_sequence = []

    while zero_indegree:
        node = zero_indegree.popleft()
        topo_sequence.append(node)
        for adj in adjacency_list[node]:
            incoming_edges[adj] -= 1
            if incoming_edges[adj] == 0:
                zero_indegree.append(adj)

    
    total_nodes = row_count * col_count
    if len(topo_sequence) != total_nodes:
        print("Cycle detected, topological order not possible.")
    else:
        print("Topological Order of Robot Traversal:")
        for step in topo_sequence:
            print(step)

robot_topo_sort(3, 3)
