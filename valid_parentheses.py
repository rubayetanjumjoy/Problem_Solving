def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        a=['(','{','[']
        b=[')','}',']']
        stack=[]
       
        for char in s:
            if char in a:
                stack.append(char)
            else:
                if not stack:
                    return False
                if a[b.index(char)]==stack[-1]:
                    stack.pop()
                else:
                    return False
                
        if len(stack)==0:
            return True
            
        else:
            return False
print(isValid('()'))