import math
# Closest pair using brute force
def closest_pair(points):
    min_dist = float('inf')
    pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.dist(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return pair, min_dist

# Convex hull using brute force
def convex_hull(points):
    hull = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            left = right = False
            for k in range(len(points)):
                if k != i and k != j:
                    # Calculate orientation
                    cross = (points[j][1] - points[i][1]) * (points[k][0] - points[j][0]) - \
                            (points[j][0] - points[i][0]) * (points[k][1] - points[j][1])
                    if cross > 0: left = True
                    elif cross < 0: right = True
                if left and right: break
            # Add points to hull if they form a boundary
            if not (left and right):
                if points[i] not in hull: hull.append(points[i])
                if points[j] not in hull: hull.append(points[j])
    return sorted(hull)

# Sample points
points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]

# Results
pair, dist = closest_pair(points)
hull = convex_hull(points)

print("Closest pair:", pair)
print("Minimum distance:", dist)
print("Convex Hull points:", hull)

Output:
Closest pair: ((9, 3.5), (7.5, 4.5))
Minimum distance: 1.8027756377319946
Convex Hull points: [(5, 3), (6, 6.5), (10, 0), (12.5, 7), (15, 3)]
