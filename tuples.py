from collections import Counter
def count_tuples(A, B, C, D):
    ab_sum = Counter(a + b for a in A for b in B)
    return sum(ab_sum[-(c + d)] for c in C for d in D)
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
# Output the result
print(count_tuples(A, B, C, D))
