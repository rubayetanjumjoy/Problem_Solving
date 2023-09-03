def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums=set(nums)
        print(nums)
        print(set_nums)
        max_sub=0
       
        for ele in nums:
            sub=0
            if ele-1  not in set_nums:
                
                while ele in set_nums:
                    ele+=1
                    sub+=1
                max_sub=max(sub,max_sub)
        return max_sub
            
print(longestConsecutive([1,2,5,4,100,1]))