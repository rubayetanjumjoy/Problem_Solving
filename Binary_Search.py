def binarySearch(find,List):
     
     
    f=0
    mid=0
    l=len(List)-1
    while f<=l:
        print(f,l)
        mid=(f+l)//2 
        print(mid,'mid')
        # 2
        
        if List[mid]==find:
            return List[mid],mid
        if List[mid]>find:
            l=mid
            print('last',mid)
        if List[mid]<find:
            f=mid-1
            print('first',mid)
        
print(binarySearch(5,[1,2,3,4,5,6,7,8]))
