'''Describe the Selection Sort algorithm's process of sorting an array. Selection Sort works by dividing the array into a sorted and an unsorted
region. Initially, the sorted region is empty, and the unsorted region contains all elements. The algorithm repeatedly selects the smallest element
from the unsorted region and swaps it with the leftmost unsorted element, then moves the boundary of the sorted region one element to the right.
Explain why Selection Sort is simple to understand and implement but is inefficient for large datasets. Provide examples to illustrate step-by-step how
Selection Sort rearranges the elements into ascending order, ensuring clarity in your explanation of the algorithm's mechanics and effectiveness.'''

arr=[5,2,9,1,5,6]
for i in range(len(arr)):
    min_index=i
    for j in range(i+1, len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)

Output: [1, 2, 5, 5, 6, 9]
