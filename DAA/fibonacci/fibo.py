import time

recursive_count = 0
def fib_recursive(n):
    global recursive_count
    recursive_count += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

non_recursive_count = 0
def fib_non_recursive(n):
    global non_recursive_count
    if n == 0:
        return
    if n >= 1:
        non_recursive_count += 1  # for printing 0th element
        print(0, end=" ")
    if n >= 2:
        non_recursive_count += 1  # for printing 1st element
        print(1, end=" ")

    n1, n2 = 0, 1
    for i in range(2, n):
        non_recursive_count += 1   # counting each addition step
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
    print()

def main():
    n = int(input("Enter the number of elements : "))

    print("\nFibonacci Sequence (Non Recursive): ", end="")
    start1 = time.time()
    fib_non_recursive(n)
    end1 = time.time()
    time_non_recursive = (end1 - start1) * 1_000_000  # microseconds

    print("\nFibonacci Sequence (Recursive): ", end="")
    start2 = time.time()
    for i in range(n):
        print(fib_recursive(i), end=" ")
    end2 = time.time()
    time_recursive = (end2 - start2) * 1_000_000  # microseconds

    # ---------- Time & Space Complexity ----------
    print("\n=== Time and Space Complexity Analysis ===")
    print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
    print("Recursive Time Complexity: O(2^n)")
    print("Recursive Space Complexity: O(n)\n")

    print(f"Non-Recursive Time Taken: {time_non_recursive:.2f} microseconds")
    print("Non-Recursive Time Complexity: O(n)")
    print("Non-Recursive Space Complexity: O(1)")

        # --- ADD/REPLACE THESE LINES ---
    print("\n\n--- 📊 Complexity Analysis ---")
    
    print("\n--- Non-Recursive (Iterative) ---")
    print("Full (un-simplified) Time: O(n)")
    print("Full (un-simplified) Space: O(1)")
    print("Final (dominant) Time: O(n)")
    print("Final (dominant) Space: O(1)")

    print("\n--- Recursive (as used in main) ---")
    print("Full (un-simplified) Time: O(2^0 + 2^1 + ... + 2^(n-1))")
    print("Full (un-simplified) Space: O(n) (for max stack depth)")
    print("Final (dominant) Time: O(2^n)")
    print("Final (dominant) Space: O(n)")
    
    print("\n--- Counts & Timers ---")
   # print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
    # print(f"Non-Recursive Time Taken: {time_non_recursive:.2f} microseconds")
    print(f"Recursive Steps (function calls): {recursive_count}")
    print(f"Non-Recursive Steps (loop iterations): {non_recursive_count}")
    # -----------------------------------


    print(f"Recursive Steps: {recursive_count}")
    print(f"Non-Recursive Steps: {non_recursive_count}")

if __name__ == "__main__":
    main()

