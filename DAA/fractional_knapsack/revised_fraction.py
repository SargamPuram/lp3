def fractionalKnapsack(W, profits, weights):
    n = len(profits)

    items = []
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append([ratio, profits[i], weights[i], i + 1])

    for i in range(n):
        for j in range(i + 1, n):
            if items[j][0] > items[i][0]:
                items[i], items[j] = items[j], items[i]

    finalValue = 0.0
    filledWeight = 0
    selected = []

    for ratio, profit, weight, idx in items:
        if W >= weight:
            finalValue += profit
            W -= weight
            filledWeight += weight
            selected.append(f"<{idx}>")
        else:
            fraction = W / weight
            finalValue += profit * fraction
            filledWeight += W
            selected.append(f"<{fraction:.2f} * {idx}>")
            break

    return finalValue, filledWeight, selected

def main():
    # Take number of items from user
    n = int(input("Enter number of items: "))

    profits = []
    weights = []

    print("Enter profits and weights of each item:")
    for i in range(n):
        p = float(input(f"Profit of item {i+1}: "))
        w = float(input(f"Weight of item {i+1}: "))
        profits.append(p)
        weights.append(w)

    # Take capacity input
    W = float(input("Enter capacity of knapsack: "))

    value, filled, items = fractionalKnapsack(W, profits, weights)

    print("\nMaximum profit:", value)
    print("Weight filled:", filled)
    print("Items selected:", ", ".join(items))

if __name__ == "__main__":
    main()
