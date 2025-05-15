class Node:
    def __init__(self, a,b,z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 9999
        self.state = 0

    def init(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        self.N = len(graph)
        source_x = 0
        source_y = 2
        goal_x = 4
        goal_y = 4
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, self.goal_level)
        self.st_dfs(graph, self.source)

        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal.depth)
        else:
            print("Goal cannot be reached from the starting block")

    def print_direction(self, m, x, y):
        if m == 0:
            print("Moving Down ({}, {})".format(x,y))
        elif m == 1:
            print("Moving Up ({}, {})".format(x,y))
        elif m == 2:
            print("Moving Right ({}, {})".format(x,y))
        else:
            print("Moving Left ({}, {})".format(x,y))

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            if (0 <= v_x < self.N) and (0 <= v_y < self.N) and (graph[v_x][v_y]) == 1:
                v_depth = u.depth + 1
                self.print_direction(j,v_x,v_y)

                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    return

                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
            if self.found:
                return

d = DFS()
d.init()
