def fractionalKnapsack(W, profits, weights):
    n = len(profits)

    # Build list of (ratio, profit, weight, index)
    items = []
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append([ratio, profits[i], weights[i], i + 1])

    # Sort items by ratio (descending)
    for i in range(n):
        for j in range(i + 1, n):
            if items[j][0] > items[i][0]:
                items[i], items[j] = items[j], items[i]

    finalValue = 0.0
    filledWeight = 0
    selected = []

    for ratio, profit, weight, idx in items:
        if W >= weight:
            # Take full item
            finalValue += profit
            W -= weight
            filledWeight += weight
            selected.append(f"<{idx}>")
        else:
            # Take fractional part
            fraction = W / weight
            finalValue += profit * fraction
            filledWeight += W
            selected.append(f"<{fraction:.2f} * {idx}>")
            break

    return finalValue, filledWeight, selected

def main():
    # Test input - you can change these values during practical
    profits = [200, 180, 120]
    weights = [20, 30, 10]
    W = 50

    value, filled, items = fractionalKnapsack(W, profits, weights)

    print("Maximum profit:", value)
    print("Weight filled:", filled)
    print("Items selected:", ", ".json(items))

    # --- ADD THESE LINES ---
    print("\n--- 📊 Complexity Analysis (for this code) ---")
    print("Full (un-simplified) Time: O(n^2 + n)")
    print("Full (un-simplified) Space: O(n + n)")
    print("\nFinal (dominant) Time: O(n^2)")
    print("Final (dominant) Space: O(n)")
    print("(where n = number of items)")
    # -----------------------

if __name__ == "__main__":
    main()
