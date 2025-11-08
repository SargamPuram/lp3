import sys

sys.setrecursionlimit(2000)

# --- Global Configuration ---
global N
N = 8

global INITIAL_ROW
global INITIAL_COL
INITIAL_ROW = 1  
INITIAL_COL = 0

# --- Global Variables for Tracing ---
step_counter = 0

first_branch_trace_active = True

def print_trace_step(board, col_index, action):
    """Prints a single step of the backtracking trace."""
    global step_counter
    step_counter += 1
    print(f"\n--- Step {step_counter}: Col {col_index}. {action} ---")
    for row in board:
        # Use 'Q' for queens and '.' for empty squares for better readability
        print(" ".join(['Q' if cell == 1 else '.' for cell in row]))

def print_final_board(board):
    """Prints the final solution board cleanly."""
    for row in board:
        print(" ".join(['Q'if cell == 1 else '.' for cell in row]))

def isSafe(board, row, col):
    """Checks if a queen can be safely placed at board[row][col]."""
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    """
    Recursive utility to place queens.
    'col' is the current column being processed.
    """
    global first_branch_trace_active

    # Base case: If all queens are placed, we have a solution.
    if col >= N:
        return True

    # Skip the column where the initial queen is placed
    if col == INITIAL_COL:
        if first_branch_trace_active:
            print_trace_step(board, col, f"SKIP: Initial Queen is fixed at ({INITIAL_ROW}, {INITIAL_COL})")
        return solveNQUtil(board, col + 1)

    # Try placing a queen in all rows of the current column
    for i in range(N):
        if isSafe(board, i, col):
            
            # 1. PLACE QUEEN (Tentative Decision)
            board[i][col] = 1
            if first_branch_trace_active:
                print_trace_step(board, col, f"Place Queen at ({i}, {col})")
            
            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True
                
            # 2. BACKTRACK (Undo Decision)
            # This part is reached only if the recursive call above failed.
            board[i][col] = 0
            if first_branch_trace_active:
                print_trace_step(board, col, f"BACKTRACK: Removing Queen at ({i}, {col})")
                # CRITICAL: We have backtracked. Stop tracing any further attempts.
                first_branch_trace_active = False

    # If all rows in this column fail, return False to backtrack further
    return False

def solveNQ():
    """Initializes the board and starts the solver."""
    global step_counter, first_branch_trace_active
    step_counter = 0
    first_branch_trace_active = True
    
    print(f"--- N-Queens (N={N}) Backtracking Trace of First Branch ---")
    print(f"Initial Queen Fixed at: (Row {INITIAL_ROW}, Col {INITIAL_COL})")
    
    # Initialize the board with zeros
    board = [[0] * N for _ in range(N)]

    # Place the first queen
    if not (0 <= INITIAL_ROW < N and 0 <= INITIAL_COL < N):
        print("\nError: Initial position is out of bounds.")
        return False
        
    board[INITIAL_ROW][INITIAL_COL] = 1
    
    # Start the solving process from column 0
    if solveNQUtil(board, 0) == False:
        print("\n" + "="*40)
        print("--- Final Result ---")
        print(f"Solution does not exist for N={N} with initial queen at ({INITIAL_ROW}, {INITIAL_COL}).")
        print("="*40)
        return False

    
    # If a solution was found, print it cleanly at the end.
    print("\n... (omitting further trace steps) ...")
    print("\n" + "="*40)
    print("--- Final Result ---")
    print("Solution Found!")
    print_final_board(board)
    print("="*40)
    
    return True

# --- Driver Code ---
solveNQ()