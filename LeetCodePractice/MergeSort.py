'''
Merge Sort 归并排序
Merge sort is a divide-and-conquer algorithm.
It recursively splits the array into two halves, sorts each half separately,
 then merges the two sorted subarrays into one sorted array.
 归并排序是分治算法：递归把数组对半拆分，分别排序两个子数组，最后把两个有序子数组合并成一个有序数组。


 Normally do NOT need special handling for odd or even array lengths in merge sort.
'''

def merge_sort(need_sort:list[int])->list[int]:
    arr = need_sort.copy()

    # divide list
    # find zhe middle element for the arr

    if len(arr) > 2:
        middle_pos: int = len(arr)//2
        pre_arr = merge_sort(arr[:middle_pos])
        sub_arr = merge_sort(arr[middle_pos:])

        if pre_arr[len(pre_arr)-1] <= sub_arr[0]:
            return pre_arr + sub_arr

        if sub_arr[len(sub_arr)-1] <= pre_arr[0]:
            return sub_arr + pre_arr

        new_arr = []
        # merge the two arr
        # Python list is dynamic array, not a real queue.
        new_idx = 0
        pre_had_insert_idx = 0
        sub_had_insert_idx = 0
        while pre_had_insert_idx < len(pre_arr) and sub_had_insert_idx < len(sub_arr):

                val1 = pre_arr[pre_had_insert_idx]
                val2 = sub_arr[sub_had_insert_idx]
                if val1 < val2:
                    new_arr.insert(new_idx,val1)
                    pre_had_insert_idx += 1
                elif val1 == val2:
                    new_arr.insert(new_idx, val1)
                    pre_had_insert_idx += 1
                    new_idx += 1
                    new_arr.insert(new_idx, val2)
                    sub_had_insert_idx += 1

                else:
                    new_arr.insert(new_idx, val2)
                    sub_had_insert_idx += 1

                new_idx += 1

        # 将剩余的队列压入新队列
        while pre_had_insert_idx <= len(pre_arr) - 1:
            new_arr.insert(new_idx, pre_arr[pre_had_insert_idx])
            pre_had_insert_idx += 1
            new_idx += 1

        while sub_had_insert_idx <= len(sub_arr) - 1:
            new_arr.insert(new_idx, sub_arr[sub_had_insert_idx])
            sub_had_insert_idx += 1
            new_idx += 1

        return new_arr


    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0] = arr[0] ^ arr[1]
            arr[1] = arr[0] ^ arr[1]
            arr[0] = arr[0] ^ arr[1]

    return arr


if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    # need_sort = [5,7,1,12,31,77,9,5]
    # need_sort = [5, 7, 7, 5]
    print(f" before sort-->", need_sort)
    sorted = merge_sort(need_sort)
    print(f"sorted-->", sorted)
