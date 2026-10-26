'''
Merge Sort 归并排序
Merge sort is a divide-and-conquer algorithm.
It recursively splits the array into two halves, sorts each half separately,
 then merges the two sorted subarrays into one sorted array.
 归并排序是分治算法：递归把数组对半拆分，分别排序两个子数组，最后把两个有序子数组合并成一个有序数组。


 Normally do NOT need special handling for odd or even array lengths in merge sort.
'''

def merge_sort_by_myself(need_sort:list[int])->list[int]:

    '''
    ### ug 1: Base case wrong

        Your condition is `if len(arr) > 2`.
        你的递归判断是 `if len(arr) > 2`
        That means:

        - len = 1 → directly return arr ✅
        - len = 2 → enter elif block, swap if out of order ✅
        - len = 3,4,5... → go split ✅
        But **the recursion base case standard convention is `len(arr) <= 1`**.
        但标准基线条件是 `len(arr) <= 1`。
        Your code works now, but it is easy to make mistakes when extending.
        你现在能跑，但属于非标写法，面试考官会指出来。

        ### Bug 2: Using `.insert(new_idx, val)` inside merge

        ```
        new_arr.insert(new_idx,val1)
        ```

        `list.insert()` is **O(n)** every time.
        每一次 `insert` 都是 O (n)。
        Standard merge sort uses append (amortized O (1)), which is the expected implementation.
        标准归并合并阶段只用 `append()`（均摊 O (1)），这是面试期望写法。
        Your merge part degrades time complexity in practice.
        你这里会拉低合并阶段实际效率。

        ### Bug 3: XOR swap for two integers

        ```
        arr[0] = arr[0] ^ arr[1]
        arr[1] = arr[0] ^ arr[1]
        arr[0] = arr[0] ^ arr[1]
        ```

        XOR swap fails when two variables point to the **same memory address**.
        异或交换有坑：两个变量指向同一个内存位置时直接归零。
        In Python, simple swap `arr[0], arr[1] = arr[1], arr[0]` is clean and safe, interview preferred.
        Python 优先写 `arr[0], arr[1] = arr[1], arr[0]`，简洁安全，面试首选。

        ### Bug 4: Equal branch logic

        ```
        elif val1 == val2:
            new_arr.insert(new_idx, val1)
            pre_had_insert_idx += 1
            new_idx += 1
            new_arr.insert(new_idx, val2)
            sub_had_insert_idx += 1
            new_idx += 1
        ```

        Functionally it is correct, but redundant.
        功能没问题，但代码冗余。
        You can just let `val1 <= val2` handle equality naturally.
        完全可以合并到 `val1 <= val2` 分支统一处理相等情况。

        ### Bug 5: Missing return for len=2 sorted case

        When `len(arr)==2` and `arr[0] <= arr[1]`, you fall through and `return arr`, that part is okay, but the structure is not clean.
        长度等于 2 且本身有序时，会落到最后的 return，结果正确，但结构不干净。

        ## 📌 Test case to verify

        ```
        print(merge_sort([5,3,8,3,2]))
        print(merge_sort([2,2,2]))
        print(merge_sort([9,8,7,6]))
        ```

    '''

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
