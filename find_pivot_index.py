def pivotIndex( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left_sum=0
    total=sum(nums)
    for i in range(len(nums)):
       
        right_sum=total-nums[i]-left_sum

        if left_sum==right_sum:
            print('found',i)
            return i 
            
        left_sum+=nums[i]
    return -1

pivotIndex([1,3,1,1,3])