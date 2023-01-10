def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    hashtable={}
    for word in strs:
        key_sorted="".join(sorted(word))
        print(key_sorted)
        if key_sorted not in hashtable:
            hashtable[key_sorted]=[word]
        else:
            hashtable[key_sorted].append(word)
        
        
    print(hashtable.values())
         
         
    


groupAnagrams(["eat","tea","tan","ate","nat","bat"])
