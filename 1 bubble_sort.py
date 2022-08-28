arr = [4, 3, 5, 2, 1, 7]


def bubble_sort(arr):  # 定义一个冒泡排序法的函数
    """
    大致思路是：对含有n个数的一个列表，一共进行n-1次循环，每次循环实现的是把当前循环最大的数排到最后。
    排序的思路是：前一个和后一个数比较：如果前者大，调换；如果前者小，不作改变。同样可以利用循环实现，并且，每一次循环比较次数少1。
    优化方案：进入第一个循环后默认不改变顺序，设置变量为False：若比较大小时改变顺序了，则设置变量为True；若没改变顺序，则退出该循环到下一个。

    """
    n = len(arr)
    for i in range(0, n-1):
        change = False
        print("第 i = ", i, "趟排序")
        for j in range(0, n-1-i):
            print("j=", j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("第", j+1, "次比较的结果", arr)
                change = True
            else:
                print("——————————————————")
        if not change:
            break


bubble_sort(arr)

