class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        a=[a,b,a,3]
        a.pop(2)
        a.pop(1)
        
        """
        def buildString(s):
            stack = []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        
        return buildString(s) == buildString(t)
    
print(Solution().backspaceCompare('ab#b','aa#b'))