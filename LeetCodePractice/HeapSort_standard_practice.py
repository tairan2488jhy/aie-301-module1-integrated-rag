
def heapify_down(arr:list[int], node:int, n:int)-> None:
    current = node
    left = 2 * node + 1
    right = 2 * node + 2

    if left < n and arr[left] > arr[current]:
        current = left
    if right < n and arr[right] > arr[current]:
        current = right

    if current != node:
        arr[current],arr[node] = arr[node],arr[current]
        heapify_down(arr,current,n)


def heap_sort(arr:list[int])->None:
    n = len(arr)

    # create top max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr,i,n)

    # exctract from max top heap
    for j in range(n):
        arr[0],arr[n-1-j]=arr[n-1-j],arr[0]
        heapify_down(arr,0,n-1-j)

if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print("the list need to sort-->",need_sort)
    heap_sort(need_sort)
    print("the sorted list -->",need_sort)