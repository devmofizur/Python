def binary_search1(list, item): #Approach 1 : check mid with item
    if len(list) == 0:
        return "Not Found"
    
    mid = len(list)//2
    if list[mid] == item:
        return f"Found"
    elif item < list[mid]:
        return binary_search1(list[:mid],item)
    elif item > list[mid]:
        return binary_search1(list[mid+1:],item)

def binary_search2(list, item): #Approach 2 : move mid index according to item
    left_index = 0
    right_index = len(list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]
        
        if mid_number == item:
            return mid_index
        elif mid_number < item:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return "Not found"



if __name__ == "__main__":
    list = [4,2,0,66,9,8,14,16,19,11,7,15]
    sorted_list = [0,2,4,7,8,9,11,14,15,16,19,66]
    search = 19

    print("Binary Search result : ", binary_search2(sorted_list , search))

