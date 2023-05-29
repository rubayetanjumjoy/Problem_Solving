def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_set={}
        for ele in nums:
            hash_set[ele]=hash_set.get(ele,0)+1
        counter=0
        for key,value in hash_set.items():
            
            print(key,value)
        results=[]
        for i in range(k):
            top_frequent_element = max(hash_set, key=hash_set.get)
            results.append(top_frequent_element)
            print(top_frequent_element)
            hash_set.pop(top_frequent_element)
        return results
print(topKFrequent([1,2,1,2,1],2))