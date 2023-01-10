def searchInsert(nums, target):
        """
        11<9?
        [1,5,7,9]
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            midpoint = (first + last)//2
            if  target==nums[midpoint]:
                return midpoint
            elif nums[midpoint] < target:
                first = midpoint+1
            else:
                last = midpoint-1
        print(first)
        return first
searchInsert([1,3,5,6],2)