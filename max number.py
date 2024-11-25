#Write a program FOR THE BELOW TEST CASES with least time complexity Test Cases: 1) Input: {1, 2, 3, 4, 5} Expected Output: 5
nums = [-10, 2, 3, -4, 5]
max_value = nums[0]
for num in nums:
    if num > max_value:
        max_value = num
print(max_value)  

# Output: 5
