'''
Bubble sort repeatedly scans the array, compares adjacent elements,
 and swaps them if they are in the wrong order. Larger elements "bubble"
 toward the end of the array in each pass.
 冒泡排序重复遍历数组，比较相邻两个元素，
 如果顺序错误就交换；每一轮会把较大元素逐步“冒泡”到数组尾部。
'''



def bubble_sort_from_min(need_sort: list[int])->list[int]:
    arr = need_sort.copy()
    idx = 1
    while idx < len(arr):
        idx2 = len(arr) - 1
        while idx2 >= idx:
            if arr[idx2-1] > arr[idx2]:
                arr[idx2-1],arr[idx2] = arr[idx2],arr[idx2-1]
            idx2 -= 1

        idx += 1


    return arr







def bubble_sort_from_min_v1(need_sort: list[int])->list[int]:
    arr = need_sort.copy()

    idx = 1
    while idx < len(arr):
        idx2 = len(arr) - 1
        while idx2 >= idx:
            if arr[idx2-1] > arr[idx2]:
                arr[idx2-1],arr[idx2] = arr[idx2],arr[idx2-1]
            idx2 -= 1

        idx += 1

    return arr


if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    print(f" before sort-->", need_sort)
    # sorted = insertion_sort_from_min(need_sort)
    sorted = bubble_sort_from_min(need_sort)
    print(f"sorted-->", sorted)