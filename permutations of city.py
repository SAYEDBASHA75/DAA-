import itertools
import math
cities=[(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
min_distance=float('inf')
for perm in itertools.permutations(cities[1:]):
    current_path=[cities[0]] + list(perm)
    total_distance=0
    for i in range(len(current_path) - 1):
        total_distance += math.sqrt((current_path[i][0] - current_path[i+1][0]) ** 2 + (current_path[i][1] - current_path[i+1][1]) ** 2)
    if total_distance<min_distance:
        min_distance=total_distance
        best_path=current_path
print("Shortest path:", best_path)
print("Minimum Distance:", min_distance)

Output:
Shortest path: [(2, 4), (1, 7), (5, 9), (6, 3), (8, 1)]
Minimum Distance: 16.54560327021237
