 from itertools import combinations

def knapsack(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = []

    # Check all combinations of items
    for r in range(n + 1):
        for combo in combinations(range(n), r):
            total_weight = sum(weights[i] for i in combo)
            total_value = sum(values[i] for i in combo)
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_combination = list(combo)

    return best_combination, max_value

# Test Case 1
weights = [2, 3, 1]
values = [4, 5, 3]
capacity = 4

selection, total = knapsack(weights, values, capacity)
print("Optimal Selection:", selection)
print("Total Value:", total)

Output:
Optimal Selection: [1, 2]
Total Value: 8
