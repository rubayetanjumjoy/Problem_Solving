# [[1,3],[4,8],[15,30],[50,60]],[5,7]

# new interver[4,8] // [15,30]
# logic
# new=[1,3],[4,5],[6,7] 3<4 append and 1<5 

def insert(intervals,newInterval):
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
    res.append(newInterval)
    return res
   

        
print(insert([[50,60],[1,3],[4,8],[-15,20],[15,10]],[5,7]))