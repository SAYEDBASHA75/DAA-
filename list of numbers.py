'''6) You have an algorithm that process a list of numbers. It firsts sorts the list using an efficient sorting algorithm and then finds the maximum element in sorted list. 
Write the code for the same'''
numbers = [3, 3, 3, 3, 3]  
if not numbers:
    print("List is empty")
else:
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    max_element = numbers[-1]
    print(max_element)

Output:3
