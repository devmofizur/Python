#--Approach 1--Easy to understand but need more space in memory
# def quick_sort(list): 
#     if len(list)<=1:
#         return list
#     else:
#         pivot = list.pop()

#     items_greater = []
#     items_lower = []

#     for items in list:
#         if items > pivot:
#             items_greater.append(items)
#         else:
#             items_lower.append(items)
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


#--Approach 2-- In Plane : Efficient Method
def swap(i,j,list):
    if i!=j:
        temp = list[i]
        list[i] = list[j]
        list[j] = temp

def partitioning(list, start,end):
    pivot_index = start
    pivot = list[pivot_index]

    while(start<end):
        while start < len(list) and list[start] <= pivot:
            start+=1
        while list[end] > pivot:
            end-=1

        if start < end:
            swap(start,end,list)
    swap(pivot_index,end,list)
    
    return end
    

def quick_sort(list,start,end):
    if start < end:
        partition_index = partitioning(list,start,end)
        quick_sort(list,start,partition_index-1)
        quick_sort(list,partition_index+1,end)
    
    return list

if __name__ == "__main__":
    list = [1, 18, 994, 56, 237, 810, 44, 672, 129, 3, 550, 881, 34, 912, 102, 67, 431, 725, 19, 2]

    print("sorted list : ",quick_sort(list,0,len(list)-1))