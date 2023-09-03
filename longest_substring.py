s="abcabczz"


char_set=set()
l=0

max_len=0
for r in range(len(s)):
    while s[r] in char_set:
        char_set.remove(s[l])
        l+=1
    
    char_set.add(s[r])
    print(s[l:r+1])
    max_len=max(max_len,r-l+1)
    if len(s[l:r+1])==max_len:
        value=s[l:r+1]
    
print(value,"max")
print(max_len)