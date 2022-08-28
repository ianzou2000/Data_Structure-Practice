# list = [49, 36, 13]
#
# t = list[1]
# if list[0] > t:
#     list[1] = list[0]
#     list[0] = t
#
# t = list[2]  # 索引取到len(list)-1
# if list[1] > t:  # 这里可以改成while循环，循环次数为取出的索引数
#     list[2] = list[1]
#     if list[0] > t:  # 次数每次减1
#         list[1] = list[0]
#         list[0] = t
# print(list)


def InsertSort(l):
    for i in range(1, len(l)):
        t = l[i]
        j = i
        while j > 0 and l[j-1] > t:
            l[j] = l[j-1]
            j -= 1
        l[j] = t
    print(l)


l = [49, 38, 65, 97, 76, 13, 27, 49]
InsertSort(l)