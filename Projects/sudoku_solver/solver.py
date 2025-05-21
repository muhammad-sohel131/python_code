import time

# Global step counter
solve_steps = 0

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def solve(board):
    global solve_steps
    solve_steps = 0
    start_time = time.time()
    result = _solve(board)
    end_time = time.time()
    return result, solve_steps, round(end_time - start_time, 4)

def _solve(board):
    global solve_steps
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        solve_steps += 1
                        if _solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def select_unassigned_variable_mrv(board, domains):
    min_domain_size = 10 
    selected = None

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                domain_size = len(domains[row][col])
                if domain_size < min_domain_size:
                    min_domain_size = domain_size
                    selected = (row, col)
    return selected



def csp_backtrack(board, domains):
    global solve_steps

    empty = select_unassigned_variable_mrv(board, domains)
    if not empty:
        return True  # Solved

    row, col = empty

    for value in domains[row][col]:
        if is_valid(board, row, col, value):
            board[row][col] = value
            solve_steps += 1

            # Create a deep copy of domains to simulate forward checking
            new_domains = [ [list(domains[r][c]) for c in range(9)] for r in range(9) ]
            new_domains[row][col] = [value]  # Set current cell domain to only the chosen value

            result = csp_backtrack(board, new_domains)
            if result:
                return True

            board[row][col] = 0

    return False



def solve_csp(board):
    global solve_steps
    solve_steps = 0
    import time
    start = time.time()

    domains = [[[i for i in range(1, 10)] for _ in range(9)] for _ in range(9)]

    result = csp_backtrack(board, domains)

    end = time.time()
    duration = end - start

    return result, solve_steps, duration


