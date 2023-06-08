a="ab"
b="eiaboo"

def checkInclusion( s1, s2):
   """
   :type s1: str
   :type s2: str
   :rtype: bool
   """   
   hash_s1={}
   hash_s2={}
   for char in s1:
      hash_s1[char]=hash_s1.get(char,0)+1
   start=0
   end=0
   
   while end <len(s2):
      hash_s2[s2[end]]=hash_s2.get(s2[end],0)+1
      print(hash_s2)
      if end-start+1==len(s1):
         if hash_s1==hash_s2:
            return True
         hash_s2[s2[start]]-=1

         if hash_s2[s2[start]]==0:
            del hash_s2[s2[start]]
         start+=1

         
      end+=1
   return False


   


print(checkInclusion(a,b))