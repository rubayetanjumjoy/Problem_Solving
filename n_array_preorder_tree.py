def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        convert_str=str(x)
        revrs=convert_str[::-1]
        if x==int(revrs):
            return True
        else:
            return False

print(isPalindrome(121))