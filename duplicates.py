'''7. Write a program that takes an input list of n numbers and creates a new list containing only the unique elements from the original list. What is
the space complexity of the algorithm?'''
def no_duplicate(nums):
    ans=[]
    for i in nums:
        if i not in ans:
            ans.append(i)
    return ans
nums=[3,7,3,5,2,5,9,2]
print(no_duplicate(nums))

Output:[3,7,5,2,9]
