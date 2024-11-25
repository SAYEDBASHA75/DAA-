def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
n = int(input("Enter the size of the array: "))
a = []
print("Enter the elements of the array:")
for _ in range(n):
    a.append(int(input()))
sorted_array = quick_sort(a)
print("Sorted array:", sorted_array)
