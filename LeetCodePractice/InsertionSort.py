

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
                print(f"fit temp_idx->",arr[temp_idx])
                print(f"fit arr[idx]->", arr[idx])
                print(f"fit temp_idx->", temp_idx)
                right_pos = temp_idx+1
                print(f"fit right_pos->", right_pos)
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



if __name__ == "__main__":
    need_sort = [23, 7, 31, 22, 5, 106, 9, 3]
    print(f" before sort-->", need_sort)
    sorted = insertion_sort_from_min(need_sort)
    print(f" sorted-->", sorted)