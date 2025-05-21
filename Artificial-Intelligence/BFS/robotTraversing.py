from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

def is_safe(row, col, matrix, seen):
    max_row, max_col = len(matrix), len(matrix[0])
    return 0 <= row < max_row and 0 <= col < max_col and matrix[row][col] != 1 and not seen[row][col]

def bfs_traversal(matrix, source, destination):
    q = deque()
    seen = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    came_from = {}

    src_x, src_y = source
    dest_x, dest_y = destination

    q.append((src_x, src_y))
    seen[src_x][src_y] = True
    came_from[(src_x, src_y)] = None

    while q:
        curr_x, curr_y = q.popleft()

        if (curr_x, curr_y) == (dest_x, dest_y):
            break

        for move_x, move_y in DIRECTIONS:
            next_x, next_y = curr_x + move_x, curr_y + move_y
            if is_safe(next_x, next_y, matrix, seen):
                q.append((next_x, next_y))
                seen[next_x][next_y] = True
                came_from[(next_x, next_y)] = (curr_x, curr_y)

    return came_from

def trace_path(came_from, target):
    path = []

    def build_route(position):
        if position is None:
            return
        build_route(came_from[position])
        path.append(position)

    build_route(target)
    print("Path to destination:")
    for point in path:
        print(point)

# Sample 2D grid: 0 = open, 1 = blocked
matrix = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

source_position = (0, 0)
destination_position = (4, 3)

path_map = bfs_traversal(matrix, source_position, destination_position)

if destination_position in path_map:
    trace_path(path_map, destination_position)
else:
    print("No path found to destination.")
