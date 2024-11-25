def is_counter_clockwise(p1, p2, p3):
    """Check if the points p1, p2, and p3 are in counter-clockwise order.
    Uses the cross product of vectors (p2 - p1) and (p3 - p1)."""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def brute_force_convex_hull(points):
    """Finds the convex hull using the brute force approach."""
    n = len(points)
    hull = set()
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            p1, p2 = points[i], points[j]
            valid_edge = True
            for k in range(n):
                if k == i or k == j:
                    continue
                p3 = points[k]
                # If point p3 is on the right side of the line segment p1 -> p2, it's not a hull edge
                if not is_counter_clockwise(p1, p2, p3):
                    valid_edge = False
                    break
            if valid_edge:
                hull.add(p1)
                hull.add(p2)
    hull = sorted(hull, key=lambda point: (point[0], point[1]))
    return hull

points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
convex_hull = brute_force_convex_hull(points)
print("Convex Hull:", convex_hull)

Output:Convex Hull: [(0, 0), (4, 6), (8, 1)]
