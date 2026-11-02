
arr = [13,6,2,11,9,14,7,10]

# arr = [1,2,3,4]

# arr = [5,4,3,2,1]

def lomuto_partition(low:int, high:int)->int:
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1




















# Please let me maintain this function version,when i forget the core principle for Quick sort for lomuto, can pass the
# print log recover it!
def lomotu_sort_position_log_print(low:int, high:int)-> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        print(f"looping i-->", i, " j-->", j, " arr[j]-->",arr[j], " pivot --> ",pivot)
        if arr[j] <= pivot:
            i += 1
            print(f"before swaps i =",i,"<==> j =",j," arr-->",arr)
            arr[i],arr[j] = arr[j],arr[i]
            print(f"after  swaps i =",i,"<==> j =",j," arr-->", arr)
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print(f"retrun arr-->", arr)
    return i + 1
'''
1）i 是 左数组（小于pivot的数组）的下标边界
2）为什么 i+1 在 arr中肯定不会数组越界： range(low,high) 是 [low,high) 左闭右开数组，右开正好留下的是pivot的位置，因此最大的i+1 就是pivot下标

'''


if __name__ == "__main__":
    # need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    # need_sort = [5,7,1,12,31,77,9,5]
    # need_sort = [5, 7, 7, 5]
    print(f" before sort-->", arr)
    # sorted = lomotu_sort_position(0, len(arr)-1)
    sorted = lomuto_partition(0, len(arr)-1)
    print(f"sorted-->", arr)