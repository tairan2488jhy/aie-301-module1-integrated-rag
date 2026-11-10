

# Insertion sort builds the sorted sequence one element at a time.
# It takes each unsorted element and inserts it into its correct position within the already sorted prefix.
# 插入排序逐步构造有序序列，逐个取出未排序元素，将它插入前面已经排好序部分里合适的位置。

def insertion_sort_from_min(need_sort: list[int]) -> list[int]:
    global right_pos
    arr = need_sort.copy()
    idx = 1
    while idx < len(arr):
        temp_idx = idx - 1
        if arr[idx-1] < arr[idx]:# 如果当前元素比之前排序元素最后一个大，则不动
            idx += 1
            continue

        # 找到比当前元素小的第一个元素，标记位置位right_pos
        right_pos = 0
        while temp_idx >= 0:# comparation chain
            if arr[temp_idx] < arr[idx]:
                right_pos = temp_idx+1
                break
            temp_idx -= 1

        temp = arr[idx]
        pos_idx = idx - 1
        print(f"right_pos-->",right_pos)
        # 在right_pos 的后边到当前idx位置所有排序好的元素右移，腾出right_pos + 1 位置给idx
        while pos_idx > right_pos-1:
            arr[pos_idx+1] = arr[pos_idx]
            pos_idx -= 1
        arr[right_pos] = temp
        idx += 1
        print(f" temp arr-->", arr)

    return arr


def insertion_sort_from_min_doubaov1(need_sort: list[int]) -> list[int]:
    """
        Yes, this is classic insertion sort.
        是的，这就是经典插入排序。

        ### Core difference between your old code and this version
        Your first version:
        It has an extra separate loop to find the insertion position first, then another loop to shift elements.
        你上一版代码：先用一轮循环单独查找插入位置，再开一轮循环做元素后移。

        This new version:
        Combines scanning and shifting into one single while loop. While scanning backward, it shifts larger elements at the same time. This is the standard textbook style.
        这个新版本：把查找和后移合并到同一个while循环，向前扫描的同时直接完成后移，是教科书标准写法。

        ### Same essential logic (still insertion sort)
        1. We maintain `arr[0 ... i-1]` as the sorted prefix.
        我们维护 `arr[0 ... i-1]` 作为已排序前缀。
        2. Pick `arr[i]` (the first element in unsorted region) as the value to insert.
        取出 `arr[i]`（未排序区第一个元素）等待插入。
        3. Walk backwards into sorted region, move bigger elements one slot right.
        在有序区向前遍历，把更大的元素向右挪。
        4. Put the target value into `j+1` once we stop.
        停下后把待插入值放到 `j+1`。

        ### Interview key point
        Both implementations are insertion sort. They only differ in implementation details, not algorithm paradigm. The time complexity, space complexity and stability are identical.
        两种写法都属于插入排序，只是实现细节不同，算法范式没变；时间、空间复杂度、稳定性完全一致。

        - Time: Best O(n), Worst O(n²)
        - Stable: ✅ Stable
        - Space: O(n) here (because you copy input list); in-place version can be O(1)


        """

    # Insertion sort: build sorted segment from left (min side) one by one
    arr = need_sort.copy()
    # i: first index of unsorted part; arr[0..i-1] already sorted
    i = 1
    while i < len(arr):
        # take current element to insert
        current = arr[i]
        # j: end index of sorted segment, scan backward
        j = i - 1
        while j >= 0 and arr[j] > current:
            # shift bigger element to right
            arr[j + 1] = arr[j]
            j -= 1
        # insert current to correct position
        arr[j + 1] = current
        i += 1
    return arr

#Refactored clean version; Maintain my old thinking road,no global
def insertion_sort_asc_doubaoV2(need_sort: list[int]) -> list[int]:
    arr = need_sort.copy()
    idx = 1
    while idx < len(arr):
        # already in order
        if arr[idx - 1] < arr[idx]:
            idx += 1
            continue

        back_ptr = idx - 1
        insert_pos = 0
        while back_ptr >= 0:
            if arr[back_ptr] < arr[idx]:
                insert_pos = back_ptr + 1
                break
            back_ptr -= 1

        val_to_insert = arr[idx]
        shift_ptr = idx - 1
        while shift_ptr >= insert_pos:
            arr[shift_ptr + 1] = arr[shift_ptr]
            shift_ptr -= 1
        arr[insert_pos] = val_to_insert

        idx += 1
    return arr



if __name__ == "__main__":
    need_sort = [23, 7, 31, 22, 5, 106, 9, 3]
    print(f" before sort-->", need_sort)
    # sorted = insertion_sort_from_min(need_sort)
    sorted = insertion_sort_from_min_doubaov1(need_sort)
    print(f" sorted-->", sorted)