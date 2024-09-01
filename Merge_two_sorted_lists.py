def merge_sorted_list(list1,list2):
    merge_list=[]
    i=j=0
    while i <len(list1) and j <len(list2):
        if list1[i]<=list2[j]:
            merge_list.append(list1[i])
            i+=1
        else:
            merge_list.append(list2[j])
            j+=1
    merge_list.extend(list1[i:])
    merge_list.extend(list2[j:])
    return merge_list
list1=[1,3,5,7]
list2=[2,4,6]
merged_list=merge_sorted_list(list1,list2)
print(merged_list)