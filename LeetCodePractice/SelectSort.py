
# select sort just from the beginning of the list ,0~N-1,compare the max number,and place it to the position N-1;
# then ,repeat the save read and compare process, and place it to the position N-2  , and so on

# Selection sort divides the array into a sorted part and an unsorted part.
# In each iteration, it finds the minimum element from the unsorted section and
# swaps it with the first element of the unsorted section.
# 选择排序把数组分为已排序区和未排序区，每一轮在未排序区间找到最小值，和未排序区间第一个元素交换。

needSort = [23,5,31,22,7,106,9,3]

def select_sort_form_max():
    # I try to find max num
    maxvalue_idx = 0
    idx = 0
    idx2 = 1
    while idx < len(needSort) - 2:
        maxvalue = needSort[0]
        maxvalue_idx = 0
        while idx2 < len(needSort) - idx:
            if needSort[idx2] > maxvalue:
                maxvalue = needSort[idx2]
                maxvalue_idx = idx2
            idx2 += 1

        # print(f"maxvalue_idx-->",maxvalue_idx)
        # print(f"len(needSort) -1 - idx-->",len(needSort) -1 - idx)
        if maxvalue_idx != (len(needSort) -1 - idx):
            swaps(len(needSort) -1 - idx, maxvalue_idx)
        # print(f"needSort in idx loop-->", idx + 1)
        # print(f"needSort temp-->", needSort)

        idx += 1
        idx2 = 1

    return needSort


def swaps(idx1: int, idx2: int) :

    needSort[idx1] = needSort[idx1]^needSort[idx2]
    needSort[idx2] = needSort[idx1]^needSort[idx2]
    needSort[idx1] = needSort[idx1]^needSort[idx2]

    return needSort



if __name__ == "__main__":
    print(f" before sort-->", needSort)
    sorted = select_sort_form_max()
    print(f"sorted-->",sorted)