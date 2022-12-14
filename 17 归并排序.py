def merge_sort(array):  # 递归分解
    mid = int(len(array) / 2)
    if len(array) == 1:  # 递归结束的条件，分解到列表只有一个数据时结束
        return array
    list_left = merge_sort(array[:mid])
    list_right = merge_sort(array[mid:])
    print(">>>list_left:", list_left)
    print(">>>list_right:", list_right)
    return merge(list_left, list_right)  # 进行归并


def merge(list_left, list_right):  # 进行归并
    final = []
    while list_left and list_right:  # 当两个列表中任意一个为空时退出循环
        if list_left[0] <= list_right[0]:  # 如果将"<="改为"<",则归并排序不稳定
            final.append(list_left.pop(0))
        else:
            final.append(list_right.pop(0))

    return final + list_left + list_right  # 返回排序好的列表


l = [49, 38, 65, 97, 76, 13, 27, 49]
print(merge_sort(l))  # 就像是一颗二叉树一样，根节点为归并排序的结果，从叶子结点开始排序。
