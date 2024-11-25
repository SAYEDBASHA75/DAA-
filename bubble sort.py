# Write code to modify bubble_sort function to stop early if the list becomes sorted before all passes are completed.
def selection(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(0,len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swapped=True
        if not swapped:
            break
    return arr
a=[5,2,9,1,6]
print(selection(a))

Output:[1,2,5,6,9]
