# pre1=100
# curr=3

# [1,pre2,pre1,1,1,100,1,1,100,1]
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        pre2, pre1=cost[0],cost[1]
        for i in range(2,len(cost)):
            
            curr=cost[i]+min(pre1,pre2)
            print(curr)
            
            pre2=pre1
            
            pre1=curr
           
        return pre1
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))