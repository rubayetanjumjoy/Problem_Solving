list1=[2,5,6,]
list2=[1,3,9]
sorted_list=[]

i=j=0
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
       
        sorted_list.append(list1[i])
        
        i+=1
         
    else:
        sorted_list.append(list2[j])
        j+=1
sorted_list.extend(list1[i:])
sorted_list.extend(list2[j:])

print(sorted_list)

