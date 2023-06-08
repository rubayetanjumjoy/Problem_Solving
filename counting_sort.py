
arr=[1,1,3,2,1]
def countingSort(arr):
    # Write your code here
    n=max(arr)+1
    result=n*[0]
    sorted=[]
    # 0311
    for i in range(len(arr)):
        result[arr[i]]=result[arr[i]]+1
    print(result)
    for i in range(len(result)):
        for j in range(result[i]):
            sorted.append(i)
    print(sorted)



countingSort(arr)