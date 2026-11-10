'''
Bubble sort repeatedly scans the array, compares adjacent elements,
 and swaps them if they are in the wrong order. Larger elements "bubble"
 toward the end of the array in each pass.
 冒泡排序重复遍历数组，比较相邻两个元素，
 如果顺序错误就交换；每一轮会把较大元素逐步“冒泡”到数组尾部。
'''

# code manual for range method, from arr end pop min value forward!
def bubble_sort_from_min_v1(need_sort: list[int])->list[int]:
    arr = need_sort.copy()
    for i in range(len(arr)):
        j = len(arr) - 1
        while j >= 1 + i:
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                j -= 1

    return arr


def buble_sort_from_max(need_sort: list[int])->list[int]:
    arr = need_sort.copy()

    NEED_SWAPS = False
    for i in range(0, len(arr)):
        j = 0
        while j < len(arr) -1 - i:
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                NEED_SWAPS = True
            j += 1
        if not NEED_SWAPS:
            break

    return arr


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
    # need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    need_sort = [5, 7, 1, 12, 31, 77, 9, 5]
    print(f" before sort-->", need_sort)
    # sorted = insertion_sort_from_min(need_sort)
    # sorted = bubble_sort_from_min(need_sort)
    sorted = bubble_sort_from_min_v1(need_sort)
    print(f"sorted-->", sorted)