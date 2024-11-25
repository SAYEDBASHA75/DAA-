'''You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values: answer1 : the number of indices i such that nums1[i] 
exists in nums2. answer2 : the number of indices i such that nums2[i] exists in nums1 Return [answer1,answer2]'''
def checker(num1, num2):
    ans=[0,0]
    for i in num1:
        if i in num2:
            ans[0]+=1
    for i in num2:
        if i in num1:
            ans[1]+=1
    return ans
num1=[1,2,2,3,4]
num2=[2,3,4,5,6]
print(checker(num1,num2))
#Output: answer1: 4 answer2: 3
