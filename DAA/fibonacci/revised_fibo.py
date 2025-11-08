import time

recursive_count = 0
def fib_recursive(n):
    global recursive_count
    recursive_count += 1
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

memo_count = 0
def fib_memo(n, memo={}):
    global memo_count
    memo_count += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def fib_dp(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

def fib_dp_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


def main():
    n = int(input("Enter the number of elements : "))

    global recursive_count, memo_count

    # Recursive Fibonacci
    recursive_count = 0
    print("\nFibonacci Sequence (Recursive): ", end="")
    start = time.time()
    for i in range(n):
        print(fib_recursive(i), end=" ")
    end = time.time()
    print(f"\nRecursive Steps: {recursive_count}")
    print(f"Time taken (Recursive): {(end-start)*1_000_000:.2f} microseconds")

    # Memoized Fibonacci
    memo_count = 0
    memo = {}
    print("\nFibonacci Sequence (Memoized): ", end="")
    start = time.time()
    for i in range(n):
        print(fib_memo(i, memo), end=" ")
    end = time.time()
    print(f"\nMemoization Steps: {memo_count}")
    print(f"Time taken (Memoized): {(end-start)*1_000_000:.2f} microseconds")

    # DP Fibonacci
    print("\nFibonacci Sequence (DP Bottom-Up): ", end="")
    start = time.time()
    for i in range(n):
        print(fib_dp(i), end=" ")
    end = time.time()
    print(f"\nTime taken (DP): {(end-start)*1_000_000:.2f} microseconds")

    # DP Optimized Fibonacci
    print("\nFibonacci Sequence (DP Optimized): ", end="")
    start = time.time()
    for i in range(n):
        print(fib_dp_optimized(i), end=" ")
    end = time.time()
    print(f"\nTime taken (DP Optimized): {(end-start)*1_000_000:.2f} microseconds")


if __name__ == "__main__":
    main()
