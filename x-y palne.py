def kClosest(points, k):
    # Sort points based on their squared distance to the origin
    points.sort(key=lambda x: x[0]**2 + x[1]**2)
    return points[:k]

# Input
points = [[1,3], [-2,2], [5,8], [0,1]]
k = 2

# Output the result
print(kClosest(points, k))

Output:
[[0, 1], [-2, 2]]
