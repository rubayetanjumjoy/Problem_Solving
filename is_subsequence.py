def isSubsequence( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        acb
        ahbgdc
        sub=a
        
        """

        sub = ""
        for i in range(len(t)):
           
            if t[i] in s and t[i] == s[len(sub)]:
                sub += t[i]
            
        
        return sub == s
print(isSubsequence('av','aaaaav'))