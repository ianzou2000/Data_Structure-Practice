# 冒泡排序
def bubble_sort(l):
    for n in range(len(l) - 1):
        for i in range(len(l) - n - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    print(l)


l = [49, 38, 65, 97, 76, 13, 27, 49]

bubble_sort(l)