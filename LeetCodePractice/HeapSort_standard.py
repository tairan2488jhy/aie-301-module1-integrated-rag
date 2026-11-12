"""
标砖原理：
1）先建大顶堆
2）然后依据大顶堆，从堆顶向下查找分析非叶子节点，使其满足大顶堆
3）将堆顶与最后叶子节点进行交换，最大值被排到了最后，这样对于前n-1个继续执行2）和3）
"""
def heapify_down(arr:list[int], node:int, n:int):
    largest =  node
    left = 2 * largest + 1
    right = 2 * largest + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if node != largest:
        arr[node], arr[largest] = arr[largest], arr[node]
        heapify_down(arr, largest, n)

def heap_sort(arr:list[int]):
    n = len(arr)

    # create top max heap
    for i in range(n//2 - 1, -1, -1):
        heapify_down(arr,i,n)

    # extract max value from arr
    for j in range(n-1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify_down(arr,0, j)


if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print("the list need to sort-->",need_sort)
    heap_sort(need_sort)
    print("the sorted list -->",need_sort)