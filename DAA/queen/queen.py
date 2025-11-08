def print_board(board):
    for row in board:
        print(" ".join(['Q' if x == 1 else '.' for x in row]))
    print()

def is_safe(board, row, col, n):
    # Check if column contains any queen
    for i in range(n):
        if board[i][col] == 1 and i != row:
            return False
    # Check two diagonals for conflicts
    for i in range(n):
        for j in range(n):
            if i != row and j != col and board[i][j] == 1:
                if abs(row - i) == abs(col - j):
                    return False
    return True

def solve(board, row, n, solutions, fixed_row, fixed_col):
    if row == n:
        print_board(board)
        solutions[0] += 1
        return
    if row == fixed_row:
        # Skip the fixed queen's row (already placed)
        solve(board, row + 1, n, solutions, fixed_row, fixed_col)
        return
    for col in range(n):
        if col == fixed_col and row != fixed_row:
            # Skip fixed queen's column except for fixed queen's row
            continue
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, solutions, fixed_row, fixed_col)
            board[row][col] = 0

def n_queens():
    n = int(input("Enter N: "))
    r, c = map(int, input("Enter first queen position (row col): ").split())
    fixed_row, fixed_col = r - 1, c - 1
    board = [[0]*n for _ in range(n)]
    board[fixed_row][fixed_col] = 1
    print("\nInitial board:")
    print_board(board)
    print("Solutions:\n")
    solutions = [0]  # Counter for valid solutions
    solve(board, 0, n, solutions, fixed_row, fixed_col)
    print(f"Total valid solutions: {solutions[0]}")

if __name__ == "__main__":
    n_queens()
