def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            popped=s.pop(0)
            print(popped)
            s.insert(len(s)-i,popped)
        print(s)
        return s

reverseString(['h','l','o'])