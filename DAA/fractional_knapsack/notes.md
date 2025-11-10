why greedy is used here ? and explain diff between greedy and dp ?
2. Explain concept of fractional knapsack
3. Difference 
1. Why is Greedy used here?
Greedy approach is used in Fractional Knapsack because at each step, the locally optimal choice of picking the item (or fraction) with the highest profit/weight ratio leads to a globally optimal solution. This works since:

Items can be broken into fractions.

You can always pick the best piece of the remaining capacity maximizing value.

Fractional knapsack problem has the greedy-choice property and is optimal to solve greedily.

2. Difference between Greedy and Dynamic Programming (DP)
Aspect	Greedy	Dynamic Programming (DP)
Approach	Makes the best choice at each step (locally optimal)	Considers all subproblems to find best solution (globally optimal)
Problem Type	Works where greedy property holds (e.g., fractional knapsack)	Works for problems with overlapping subproblems and optimal substructure (e.g., 0/1 knapsack)
Solution	One pass, simpler, usually faster	Requires storage of subproblem solutions, more complex
Optimality	May not always give optimal solution	Guarantees optimal solution
Example Algorithm	Fractional Knapsack	0/1 Knapsack using DP table
3. Concept of Fractional Knapsack
You have items with profit and weight.

Knapsack has limited capacity.

You can take fraction of any item.

Goal: maximize total profit inside the capacity.

Sort items by profit/weight ratio.

Pick full items or fractions with highest ratio first until capacity filled.

4. Difference between Fractional and 0/1 Knapsack
Aspect	Fractional Knapsack	0/1 Knapsack
Item selection	Items can be broken; fractional parts allowed	Items indivisible; take whole or none
Approach	Greedy algorithm	Dynamic programming
Optimal substructure	Yes, supports greedy optimal substructure	Yes, requires careful state tracking
Complexity	
O
(
n
log
⁡
n
)
O(nlogn) (due to sorting)	
O
(
n
W
)
O(nW) (DP with weight capacity W)
Problem type	Continuous	Discrete
Example use case	Resource allocation, where partial use possible	Selecting projects or objects fully