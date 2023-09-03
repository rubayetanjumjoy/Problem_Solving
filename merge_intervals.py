intervals=[[1,3],[8,10],[15,18],[2,6]]
intervals.sort()

output=[intervals[0]]

for start, end in intervals[1:]:
    last_end=output[-1][1]
    if last_end>start:
        output[-1][1]=max(last_end,end)
    else:
        output.append([start,end])
print(output)