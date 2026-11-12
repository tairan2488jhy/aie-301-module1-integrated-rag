
def heapify_down(arr: list[int], start: int, heap_len: int) -> None:
    current = start
    while True:
        largest = current
        left = 2 * current + 1
        right = 2 * current + 2

        if left < heap_len and arr[left] > arr[largest]:
            largest = left
        if right < heap_len and arr[right] > arr[largest]:
            largest = right

        if largest == current:
            break  # 已经满足大顶堆，停止下沉
        # 交换父节点和最大孩子
        arr[current], arr[largest] = arr[largest], arr[current]
        current = largest  # 下沉到新位置，继续检查


def heap_sort(arr: list[int]) -> None:
    n = len(arr)
    # 建大顶堆：从最后一个非叶子节点向前遍历
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, i, n)

    # 不断取出堆顶最大值，放到数组末尾
    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify_down(arr, 0, j)






if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [4, 10, 3, 5, 1]
    # need_sort = [1,2,3,4,5,6,7]
    # need_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    # need_sort = [2,8,5,3,9,1,7,4,6]
    print("the list need to sort-->",need_sort)
    heap_sort(need_sort)
    print("the sorted list -->",need_sort)