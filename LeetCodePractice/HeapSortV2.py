from typing import Any

need_sort = []


def heap_sort_compare(current_node: int, idx: int):
    while current_node >= 0:
        if 2 * current_node + 1 < len(need_sort) - idx and need_sort[current_node] < need_sort[2 * current_node + 1]:
            need_sort[current_node], need_sort[2 * current_node + 1] = need_sort[2 * current_node + 1], need_sort[
                current_node]
            if 2 * current_node + 1 < (len(need_sort) - idx) // 2:
                heap_sort_compare(2 * current_node + 1, idx)

        if 2 * current_node + 2 < len(need_sort) - idx and need_sort[current_node] < need_sort[2 * current_node + 2]:
            need_sort[current_node], need_sort[2 * current_node + 2] = need_sort[2 * current_node + 2], need_sort[
                current_node]
            if 2 * current_node + 2 < (len(need_sort) - idx) // 2:
                heap_sort_compare(2 * current_node + 2, idx)

        current_node -= 1


def heap_sort():
    if len(need_sort) <= 1:
        return

    idx = 0
    while idx < len(need_sort):
        current_node = (len(need_sort) - idx) // 2 - 1
        heap_sort_compare(current_node, idx)
        # 交换栈顶与最后叶子节点
        need_sort[0], need_sort[len(need_sort) - 1 - idx] = need_sort[len(need_sort) - 1 - idx], need_sort[0]

        idx += 1



if __name__ == "__main__":
    # need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [2, 3, 23, 22, 9, 4, 5, 1, 18, 7, 2, 15, 20, 50, 31, 77]
    # need_sort = [1, 2, 3, 4, 5, 6, 7]
    need_sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(f" before sort-->", need_sort)
    heap_sort()
    print(f"sorted-->", need_sort)






