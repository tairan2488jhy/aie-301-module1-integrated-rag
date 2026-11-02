from typing import Any


# Time complexity=O(N²);Auxiliary space=O(N²) due to slicing and recursion
def heap_sort_self_wonderful_implement(arr:list[int])-> list[int]|None:
    '''
    Still not complete understand heap sort core,but it just can work!!
    you should know, it is not wonderful!!
    :param arr:
    :return:
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


if __name__ == "__main__":
    # need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
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
    # print(f" before sort-->", need_sort)
    # sorted = heap_sort(need_sort)
    # print(f"sorted-->", sorted)

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

    print("All tests passed!")