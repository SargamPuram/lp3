import sys
sys.setrecursionlimit(2000)

step_counter = 0
trace_active = True  # Control detailed tracing for first found solution

def print_trace_step(board, col, action):
    global step_counter
    step_counter += 1
    print(f"\n--- Step {step_counter}: Col {col}. {action} ---")
    for row in board:
        print(" ".join(['Q' if cell == 1 else '.' for cell in row]))

def print_final_board(board):
    print("\n----- Final Valid Solution Found -----")
    for row in board:
        print(" ".join(['Q' if cell == 1 else '.' for cell in row]))
    print()

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_nq_util(board, row, N, fixed_row=None, fixed_col=None):
    global trace_active

    if row == N:
        print_final_board(board)
        trace_active = False  # Stop verbose trace after first solution.
        return 1

    if fixed_row == row:
        if trace_active:
            print_trace_step(board, fixed_col, f"SKIP: Fixed Queen at ({fixed_row}, {fixed_col})")
        return solve_nq_util(board, row + 1, N, fixed_row, fixed_col)

    count = 0
    for col in range(N):
        if fixed_col is not None and row == fixed_row and col != fixed_col:
            continue
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if trace_active:
                print_trace_step(board, col, f"Place Queen at ({row}, {col})")

            count += solve_nq_util(board, row + 1, N, fixed_row, fixed_col)

            board[row][col] = 0
            if trace_active:
                print_trace_step(board, col, f"BACKTRACK: Removing Queen at ({row}, {col})")

    return count

def n_queens():
    global step_counter, trace_active
    step_counter = 0
    trace_active = True

    N = int(input("Enter board size N: "))
    fixed_pos = input("Enter fixed queen position (row col) 1-based, or press Enter to skip: ").strip()

    board = [[0] * N for _ in range(N)]
    fixed_row = fixed_col = None
    if fixed_pos:
        r, c = map(int, fixed_pos.split())
        fixed_row, fixed_col = r - 1, c - 1
        if not (0 <= fixed_row < N and 0 <= fixed_col < N):
            print("Fixed queen position out of bounds.")
            return
        board[fixed_row][fixed_col] = 1

    print(f"\n--- NQueens solutions start (N={N}) ---\n")
    total_solutions = solve_nq_util(board, 0, N, fixed_row, fixed_col)

    if total_solutions == 0:
        print("\nNo solutions found.")
    else:
        print(f"\nTotal valid solutions found: {total_solutions}")

if __name__ == "__main__":
    n_queens()

    # --- ADD THESE LINES ---
    print("\n--- 📊 Complexity Analysis (for this code) ---")
    print("Full (un-simplified) Time: O(N^2 * N!)")
    print("Full (un-simplified) Space: O(N^2 + N)")
    print("\nFinal (dominant) Time: O(N^2 * N!)")
    print("Final (dominant) Space: O(N^2)")
    print("(where N = board size)")
    # -----------------------
  