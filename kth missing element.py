#Given an array arr of positive integers sorted in a strictly increasing order, and an integer k. return the kth positive integer that is missing from this array.
def findKthPositive(arr, k):
    missing_count = 0
    current = 1
    for num in arr:
        while current < num:
            missing_count += 1
            if missing_count == k:
                return current
            current += 1
        current += 1
    return current + (k - missing_count - 1)
arr = [1,2, 3, 4]
k = 2
result = findKthPositive(arr, k)
print(f"The {k}th missing positive integer is: {result}")

Output: The 2th missing positive integer is: 6
