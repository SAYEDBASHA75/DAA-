'''Sort an array of integers using the bubble sort technique. Analyze its time complexity using Big-O notation. Write the code'''
def Bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr   
arr=[1,5,4,3,6,7]
print(Bubble_sort(arr))

Output:[10, 15, 20, 30]
