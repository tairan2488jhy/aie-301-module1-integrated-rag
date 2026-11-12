

def heap_sort_no_recursion(arr:list[int])->None:
    n = len(arr)

    # create max top heap
    for i in range(n//2 - 1, -1, -1):
        # print(f"i -->",i)
        current = i
        flag = i
        while 2 * current + 1 < n:
            # print(f"begin current-->",current)
            left = 2 *  current + 1
            right = 2 * current + 2
            if left < n and arr[left]>arr[current]:
                current = left
            if right < n and arr[right]>arr[current]:
                current = right
            # print(" 1 current-->",current,";current != i-->",current != i)
            if current != flag:
                arr[flag],arr[current] = arr[current],arr[flag]
                flag = current
            else:
                break
            # print(f"end current-->",current)
            # print(f"end i-->",i,",arr->",arr)
            ## heapify_down

    print(f"max top heap arr-->",arr)

    # extract max value from top max heap
    for j in range(n-1,0,-1):
        arr[0],arr[j] = arr[j],arr[0]
        current = 0
        flag = 0
        # print(f"begin arr-->",arr)
        while 2 * current + 1 < j:
            left = 2 *  current + 1
            right = 2 * current + 2
            if left < j and arr[left]>arr[current]:
                current = left
            if right < j and arr[right]>arr[current]:
                current = right
            # print("current-->",current,";current != i-->",current != i)
            if current != flag:
                arr[flag],arr[current] = arr[current],arr[flag]
                flag = current
            else:
                break
            # current += 1
        # print(f"end arr->",arr)




if __name__ == "__main__":
    # need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [4, 10, 3, 5, 1]
    # need_sort = [1,2,3,4,5,6,7]
    # need_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    need_sort = [2,8,5,3,9,1,7,4,6]
    print("the list need to sort-->",need_sort)
    heap_sort_no_recursion(need_sort)
    print("the sorted list -->",need_sort)