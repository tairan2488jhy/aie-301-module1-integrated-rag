
# show execute process version, can remember and understand process and principles !

show_create_heap_print = False
show_extract_max_print = False

def heapify_down(arr,size,node):
    if show_create_heap_print:
        print(f"heapify_down begin arr-->",arr,";size-->",size,";node-->",node)
    largest = node
    left = 2 * node + 1
    right = 2 * node + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != node:
        if show_create_heap_print:
            print(f"heapify_down fire switch node-->",node)
        arr[node], arr[largest] = arr[largest],arr[node]
        if largest < size // 2:
            heapify_down2(arr,size,largest)
    if show_create_heap_print:
        print(f"heapify_down end arr-->", arr, ";size-->", size, ";node-->", node)


def heapify_down2(arr, size, node):
    if show_create_heap_print:
        print(f"heapify_down2 begin arr-->", arr, ";size-->", size, ";node-->", node)
    largest = node
    left = 2 * node + 1
    right = 2 * node + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != node:
        if show_create_heap_print:
            print(f"heapify_down2 fire switch node-->", node)
        arr[node], arr[largest] = arr[largest], arr[node]
        if largest < size // 2:
            heapify_down2(arr, size, largest)
    if show_create_heap_print:
        print(f"heapify_down2 end arr-->", arr, ";size-->", size, ";node-->", node)

def heapify_down3(arr, size, node):
    if show_extract_max_print:
        print(f"heapify_down3 begin arr-->", arr, ";size-->", size, ";node-->", node)
    largest = node
    left = 2 * node + 1
    right = 2 * node + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != node:
        if show_extract_max_print:
            print(f"heapify_down3 fire switch node-->", node)
        arr[node], arr[largest] = arr[largest], arr[node]
        if largest < size//2:
            heapify_down4(arr, size, largest)

    if show_extract_max_print:
        print(f"heapify_down3 end arr-->", arr, ";size-->", size, ";node-->", node)

def heapify_down4(arr, size, node):
    if show_extract_max_print:
        print(f"heapify_down4 begin arr-->", arr, ";size-->", size, ";node-->", node)
    largest = node
    left = 2 * node + 1
    right = 2 * node + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != node:
        if show_extract_max_print:
            print(f"heapify_down4 fire switch node-->", node)
        arr[node], arr[largest] = arr[largest], arr[node]
        heapify_down4(arr, size, largest)

    if show_extract_max_print:
        print(f"heapify_down4 end arr-->", arr, ";size-->", size, ";node-->", node)


def heap_sort(arr):
    n = len(arr)

    # build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify_down(arr, n, i)

    # extract max
    for s in range(n-1, 0, -1):
        arr[0],arr[s] = arr[s],arr[0]
        heapify_down3(arr, s, 0)


if __name__ == "__main__":
    # arr = [2, 3, 23, 22, 9, 4, 5, 1, 5, 20, 50, 31, 77, 18, 7, 2, 1]
    show_create_heap_print = False
    show_extract_max_print = True
    arr = [23, 5, 31, 22, 7, 106, 9, 3]
    print("before sort -->", arr)
    heap_sort(arr)
    print("sorted -->", arr)