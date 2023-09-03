def lastStoneWeight(stones):
        """
        [1]
        2
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            stones.sort()
            a=stones.pop()
            b=stones.pop()
            stones.append(abs(a-b))
            print(stones)
        return stones[0]
print(lastStoneWeight([2,7,4,1,8,1]))