
def select_sort_form_max(need_sort: list[int])-> list[int]:

    idx = 0
    idx2 = 1
    while idx < len(need_sort) - 1:
        max_value = need_sort[0]
        max_value_idx = 0

        while idx2 < len(need_sort) - idx:
            if max_value < need_sort[idx2]:
                max_value = need_sort[idx2]
                max_value_idx = idx2
            idx2 += 1

        if len(need_sort)-1-idx != max_value_idx:

            # 错误 1（致命）：`swaps` 异或交换写法完全无效【最核心】
            #
            # Python 是**传对象引用，但 int 是不可变类型**
            #
            # ```
            # swaps(need_sort[len(need_sort)-1-idx], need_sort[max_value_idx])
            # ```
            #
            # - `need_sort[a]` 取出的是**数值副本**，不是数组里位置的引用
            # - 函数内部 `val1,val2` 只是局部变量，异或怎么改，都和原 list 无关
            #
            # >
            # > 异或交换变量的写法，**只能在同一个作用域直接交换两个变量本身**，不能把数组元素的值拿进去交换。
            # > ✅ 正确做法：直接交换下标位置

            # 交换数组下标的python特有写法
            need_sort[len(need_sort)-1-idx], need_sort[max_value_idx] = need_sort[max_value_idx], need_sort[len(need_sort)-1-idx]

        idx += 1
        idx2 = 1

    return need_sort

def swaps(val1:int, val2:int):
    val1 = val1 ^ val2
    val2 = val1 ^ val2
    val1 = val1 ^ val2


if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print(f" before sort-->", need_sort)
    sorted = select_sort_form_max(need_sort)
    print(f"sorted-->", sorted)
