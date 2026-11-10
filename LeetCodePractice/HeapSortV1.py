from typing import Any

need_sort = []

"""

这段代码**可以跑出正确有序结果**，但它依然**不是标准 heapify-down 的堆排序实现**，
遍历逻辑和标准版本有本质区别，同时有全局变量的工程问题。
标准设计是：

- 外层循环：从最后一个非叶子向前逐个调用 `heapify_down(单个节点)`
- heapify_down：只处理传入的这一个节点，只向下沉，**不向前走**
"""

def heap_sort_compare(current_node:int, idx: int) :
    print("f sub heap_sort_compare current_node-->",current_node, ";before arr-->",need_sort[0:len(need_sort) - idx])
    while current_node >= 0:
        if 2 * current_node + 1 < len(need_sort) - idx and need_sort[current_node] < need_sort[2 * current_node + 1]:
            need_sort[current_node], need_sort[2 * current_node + 1] =  need_sort[2 * current_node + 1], need_sort[current_node]
            # downtify 下沉 只有非叶子节点才有比较价值
            if 2 * current_node + 1 < (len(need_sort) - idx) // 2:
                heap_sort_compare(2 * current_node + 1, idx)


        if 2 * current_node + 2 < len(need_sort) -idx and need_sort[current_node] < need_sort[2 * current_node + 2]:
            need_sort[current_node], need_sort[2 * current_node + 2] = need_sort[2 * current_node + 2], need_sort[
                current_node]
            if 2 * current_node + 2 < (len(need_sort) - idx) // 2:
                heap_sort_compare(2 * current_node + 2, idx)

        current_node -= 1

    # print("f sub heap_sort_compare current_node-->", current_node, ";after arr-->", need_sort[0:len(need_sort) - idx])

def heap_sort():

    if len(need_sort) <= 1:
        return

    idx = 0
    while idx < len(need_sort):
        current_node = (len(need_sort) - idx) // 2 - 1
        print(f"loop idx--> ",idx,"; before main heap_sort_compare arr-->",need_sort)
        heap_sort_compare(current_node,idx)
        print(f"loop idx--> ",idx,"; after main heap_sort_compare arr-->", need_sort)

        # 交换栈顶与最后叶子节点
        need_sort[0], need_sort[len(need_sort)-1-idx] = need_sort[len(need_sort)-1-idx],need_sort[0]

        idx += 1


# Time complexity=O(N²);Auxiliary space=O(N²) due to slicing and recursion
def heap_sort_self_wonderful_implement(arr:list[int])-> list[int]|None:
    '''
    Still not complete understand heap sort core,but it just can work!!
    you should know, it is not wonderful!!
    :param arr:
    :return:
    Note: This sorting method does not follow the principle of heap sort; it is an accidental implementation.

    test_cases = [
        [],
        [1],
        [2, 1],
        [1, 2, 3],
        [1, 3, 2, 7, 6, 5, 4],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 5, 5, 5, 5],
        [-10, -5, -20, -1, -30],
        [100, -100, 0, 50, -50],
        [3, 1, 3, 2, 1, 2, 3],
        [1000, 1, 999, 2, 998, 3, 997]
    ]

    for test in test_cases:
        actual = heap_sort(test.copy())
        expected = sorted(test)

        assert actual == expected, (
            f"Failed: {test}, got {actual}"
        )

    '''

    if len(arr) == 0:
        return []


    if len(arr) <= 1:
        return arr

    no_leaf_node_count = len(arr)//2 - 1

    while no_leaf_node_count >= 0:

        if 2 * no_leaf_node_count + 1 < len(arr) and arr[no_leaf_node_count] < arr[2 * no_leaf_node_count + 1 ]:
            arr[no_leaf_node_count],arr[2*no_leaf_node_count+1] = arr[2*no_leaf_node_count+1],arr[no_leaf_node_count]

        if 2 * no_leaf_node_count + 2 < len(arr) and arr[no_leaf_node_count] < arr[2 * no_leaf_node_count + 2 ]:
            arr[no_leaf_node_count],arr[2*no_leaf_node_count+2] = arr[2*no_leaf_node_count+2],arr[no_leaf_node_count]

        no_leaf_node_count -= 1

    print(f"arr[0]-->",arr[0])

    if len(arr[1:]) == 1:
         sub_arr = arr[1:]
    else:
         sub_arr = heap_sort_self_wonderful_implement(arr[1:])

    sub_arr.append(arr[0])

    return sub_arr

"""
def heap_sort_compare(current_node:int, arr:list[int]) -> list[int]:
    print("f sub heap_sort_compare current_node-->",current_node, ";before arr-->",arr)
    while current_node >= 0:
        if 2 * current_node + 1 < len(arr) and arr[current_node] < arr[2 * current_node + 1]:
            arr[current_node], arr[2 * current_node + 1] =  arr[2 * current_node + 1], arr[current_node]
            # downtify 下沉
            heap_sort_compare(2 * current_node + 1, arr)


        if 2 * current_node + 2 < len(arr) and arr[current_node] < arr[2 * current_node + 2]:
            arr[current_node], arr[2 * current_node + 2] = arr[2 * current_node + 2], arr[
                current_node]
            heap_sort_compare(2 * current_node + 2, arr)

        current_node -= 1

    if current_node >= 0:
        print("f sub heap_sort_compare current_node-->", current_node, ";after arr-->", arr)
        
    return arr

def heap_sort(arr:list[int])->list[int]:

    if len(arr) <= 1:
        return arr


    idx = 0
    while idx < len(arr):
        current_node = (len(arr) - idx) // 2 - 1
        print(f"loop idx--> ",idx,"; before main heap_sort_compare arr-->",arr)
        arr = heap_sort_compare(current_node, arr[:len(arr) - idx])
        print(f"loop idx--> ",idx,"; after main heap_sort_compare arr-->", arr)

        # 交换栈顶与最后叶子节点
        arr[0], arr[len(arr)-1-idx] = arr[len(arr)-1-idx],arr[0]

        idx += 1


    return arr
"""

if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    # need_sort = [5, 7, 1, 12, 31, 77, 9, 5]
    # need_sort = [5, 7, 7, 5]
    # need_sort = [5, 7, 3]
    # need_sort = [4, 10, 3, 5, 1]
    # need_sort = [2, 9, 3, 7, 4, 10, 5]
    # need_sort = [6, 10, 5, 8, 7, 2, 3]
    # need_sort = [10, 18, 15, 20, 50, 80, 30, 60]
    # need_sort = [1,2,3]
    # need_sort = [4, 1, 3, 2, 5]
    # need_sort = [2, 3, 23, 22, 9, 4, 5, 1,18, 7, 2, 15, 20, 50, 31, 77]
    # need_sort = [1, 3, 2, 7, 6, 5, 4]
    # need_sort = [1, 3, 2, 7, 6, 5, 4, 8]
    print(f" before sort-->", need_sort)
    heap_sort()
    print(f"sorted-->", need_sort)






