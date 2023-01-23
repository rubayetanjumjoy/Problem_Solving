def merge_sort(arr):
    
  
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    
    return merge(left,right)

def merge(left,right):
     
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

print(merge_sort([13,2,1,4]))

# def merge_sort(arr):
#     # 1
#     print(arr)
#     if len(arr) == 1:
#         return arr
#     mid = len(arr) // 2
#     # left= 6,5
#     # right=3 1
#     # returned values 1 3 5 6
#     left_half = merge_sort(arr[:mid]) 
#     right_half = merge_sort(arr[mid:])
#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result

# print(merge_sort([6,5,3,1]))