def sort_and_find_max(numbers):
    numbers.sort()  
    max_element = numbers[-1] if numbers else None
    return max_element

numbers = []
max_value = sort_and_find_max(numbers)
print(f"The maximum element is: {max_value}")
