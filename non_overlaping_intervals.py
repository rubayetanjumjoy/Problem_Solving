class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key= lambda x: x[1])

        i = 0
        res = []
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i+1][0]:
                test = intervals.pop(i+1)
                res.append(test)
                
            else:
                i += 1
        return len(res)    
test=Solution()
print(test.eraseOverlapIntervals([[1,2],[1,3],[2,3],[3,4]]))