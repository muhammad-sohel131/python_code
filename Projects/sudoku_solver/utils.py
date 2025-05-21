import random
from solver import solve, is_valid

def generate_board(difficulty='easy'):
    board = [[0] * 9 for _ in range(9)]

    # Randomly fill a few starting cells
    filled = 0
    while filled < 10:
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0 and is_valid(board, row, col, num):
            board[row][col] = num
            filled += 1

    solve(board)  # Get a fully solved board

    # Decide how many cells to remove based on difficulty
    if difficulty == 'easy':
        cells_to_remove = 30
    elif difficulty == 'medium':
        cells_to_remove = 40
    elif difficulty == 'hard':
        cells_to_remove = 55
    else:
        cells_to_remove = 40 

    # Randomly remove cells
    removed = 0
    while removed < cells_to_remove:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            removed += 1

    return board
