
def bubble_sort(list):
    #--------Approach 1----------
    # for i in range(0,len(list)-1):
    #     for j in range(len(list)-1-i):
    #         k = j+1
    #         if list[j] > list[k]:
    #             temp = list[j]
    #             list[j] = list[k]
    #             list[k] = temp
    # return list

    #--------Approach 2----------
    # m = len(list)-1
    # for i in range(0,len(list)-1):
    #     for j in range(m):
    #         k = j+1
    #         if list[j] > list[k]:
    #             temp = list[j]
    #             list[j] = list[k]
    #             list[k] = temp
    #     m-=1
    # return list

    #--------Approach 3----------(O(n) in best case)
    for i in range(0,len(list)-1):
        swapped  = False
        for j in range(len(list)-1-i):
            k = j+1
            if list[j] > list[k]:
                temp = list[j]
                list[j] = list[k]
                list[k] = temp
                swapped = True
        if not swapped: #Breaks outer loop if list is already sorted
            break
    return list

if __name__ == "__main__":
    list = [412, 18, 994, 56, 237, 810, 44, 672, 129, 3, 550, 881, 34, 912, 102, 67, 431, 725, 19, 2]

    print("sorted list : ",bubble_sort(list))