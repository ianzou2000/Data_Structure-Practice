# 快速选择排序


def Partition(l, low, high):
    pivot = l[low]
    while low < high:
        while low < high and l[high] >= pivot:
            high -= 1
        l[low] = l[high]
        while low < high and l[low] <= pivot:
            low += 1
        l[high] = l[low]

    l[low] = pivot
    return low


def QSort(l, low, high):
    if low < high:
        pivotloc = Partition(l, low, high)
        QSort(l, low, pivotloc-1)
        QSort(l, pivotloc+1, high)
    return l


l = [49, 38, 65, 97, 76, 13, 27, 49]
low = 0
high = len(l)-1
print(QSort(l, low, high))
