'''9. Checks if a given number x exists in a sorted array arr using binary search. Analyze its time complexity using Big-O notation.'''
arr = [2, 3, 4, 10, 40]
target = 10

low, high = 0, len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target: print(f"Found at {mid}"); break
    elif arr[mid] < target: low = mid + 1
    else: high = mid - 1
else: print("Not found")

Output:Element 10 is found at position 4
