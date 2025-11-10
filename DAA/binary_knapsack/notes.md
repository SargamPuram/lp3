Concept Explanation
Each item has a profit 
p
i
p 
i
  and weight 
w
i
w 
i
 .

The "ratio" 
r
i
=
p
i
w
i
r 
i
 = 
w 
i
 
p 
i
 
  indicates how valuable an item is per unit weight.

Sort items by decreasing ratio 
r
i
r 
i
 .

Start adding items with highest ratio:

If item fits whole, take it fully.

Else take the fraction that fits.

Stop when knapsack is full.

This greedy method ensures maximum total profit.

Important Formula
r
i
=
p
i
w
i
r 
i
 = 
w 
i
 
p 
i
 
 
For partial item weight fraction 
f
f,

value added
=
p
i
×
f
,
weight added
=
w
i
×
f
value added=p 
i
 ×f,weight added=w 
i
 ×f
Code Overview from your PDF (line by line)
python
def fractionalKnapsack(W, profits, weights):
    n = len(profits)

    items = []
    for i in range(n):
        ratio = profits[i] / weights[i]            # Calculate profit to weight ratio
        items.append([ratio, profits[i], weights[i], i + 1])  # Append ratio, profit, weight, and item index

    # Sort items by ratio in descending order (greedy choice)
    for i in range(n):
        for j in range(i + 1, n):
            if items[j][0] > items[i][0]:
                items[i], items[j] = items[j], items[i]

    finalValue = 0.0
    filledWeight = 0
    selected = []

    # Iterate over sorted items
    for ratio, profit, weight, idx in items:
        if W >= weight:  # If full item fits
            finalValue += profit
            W -= weight
            filledWeight += weight
            selected.append(f"<{idx}>")
        else:  # Take fraction of item if full doesn't fit
            fraction = W / weight
            finalValue += profit * fraction
            filledWeight += W
            selected.append(f"<{fraction:.2f} * {idx}>")
            break

    return finalValue, filledWeight, selected
What is expected in the practical:
Write code to implement this logic.

Test with given inputs and print:

Maximum value obtained.

Total weight filled.

Which items were selected and if fractional, what fraction.

Understand each step (sorting, selection, fraction calculation).

Typical Viva Questions and Answers
Q1: What is the difference between 0/1 knapsack and fractional knapsack?
A: 0/1 knapsack requires entire items; fractional knapsack allows taking any fraction of an item.

Q2: Why does the greedy approach work for fractional knapsack but not always for 0/1 knapsack?
A: Because fractional knapsack's solution is continuous and can be built incrementally using the highest value/weight items. 0/1 knapsack is discrete, requiring dynamic programming.

Q3: How do you calculate the profit to weight ratio?
A: 
r
i
=
p
i
w
i
r 
i
 = 
w 
i
 
p 
i
 
 , profit divided by weight.

Q4: How do you handle the fraction of an item in this problem?
A: If remaining capacity is less than item’s weight, take 
fraction
=
remaining capacity
w
i
fraction= 
w 
i
 
remaining capacity
  and multiply the profit by this fraction.

Q5: What is the time complexity of this algorithm?
A: Sorting takes 
O
(
n
2
)
O(n 
2
 ) in your code (due to bubble sort), but it can be improved to 
O
(
n
log
⁡
n
)
O(nlogn) with efficient sorting. Selection is 
O
(
n
)
O(n), so total 
O
(
n
2
)
O(n 
2
 ) here.

If you want, I can help you improve the code, explain the sorting, or create sample practical outputs for your revision!