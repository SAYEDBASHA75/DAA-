def peak(nums):
    left,right=0, len(nums)-1
    while left<=right:
        mid= (left+ right)//2
        if (mid==0 or nums[mid]> nums[mid-1]) and (mid==len(nums)-1 or nums[mid]>  nums[mid+1]):
            print(mid)
            break
        elif mid<len(nums)-1 and nums[mid]<nums[mid+1]:
            left=mid+1
        else:
            right=mid-1
peak([1,2,1,3,5,6,4])

Output:5
