def sub_array(nums):
        maxSub=nums[0]
        curSum=0

        for n in nums:
            if curSum<0:
                curSum=0
            curSum+=n
             
            maxSub=max(maxSub,curSum)
             
        return maxSub
print(sub_array([1,2,3,1,12,3]))