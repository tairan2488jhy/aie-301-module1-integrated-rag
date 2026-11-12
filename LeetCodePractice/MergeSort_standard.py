'''
Merge Sort 归并排序
Merge sort is a divide-and-conquer algorithm.
It recursively splits the array into two halves, sorts each half separately,
 then merges the two sorted subarrays into one sorted array.
 归并排序是分治算法：递归把数组对半拆分，分别排序两个子数组，最后把两个有序子数组合并成一个有序数组。


 Normally do NOT need special handling for odd or even array lengths in merge sort.
'''


def merge_sort(need_sort: list[int]) -> list[int]:
    arr = need_sort.copy()
    if len(arr) <= 1:
        return arr

    middle_pos: int = len(arr) // 2
    pre_arr = merge_sort(arr[:middle_pos])
    sub_arr = merge_sort(arr[middle_pos:])

    # your good shortcut
    if pre_arr[-1] <= sub_arr[0]: # python index = -1 标识数组结尾的第一个元素
        return pre_arr + sub_arr
    if sub_arr[-1] <= pre_arr[0]:
        return sub_arr + pre_arr

    new_arr: list[int] = []
    i = j = 0
    while i < len(pre_arr) and j < len(sub_arr):
        if pre_arr[i] <= sub_arr[j]:
            new_arr.append(pre_arr[i])
            i += 1
        else:
            new_arr.append(sub_arr[j])
            j += 1
    new_arr.extend(pre_arr[i:])
    new_arr.extend(sub_arr[j:])
    return new_arr



if __name__ == "__main__":
    # need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    need_sort = [5,7,1,12,31,77,9,5]
    # need_sort = [5, 7, 7, 5]
    print(f" before sort-->", need_sort)
    sorted = merge_sort(need_sort)
    print(f"sorted-->", sorted)
