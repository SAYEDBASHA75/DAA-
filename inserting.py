def sorter(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(sorter([3,1,4,5,9,2,6,5,3]))
Output:[1, 2, 3, 3, 4, 5, 5, 6, 9]
