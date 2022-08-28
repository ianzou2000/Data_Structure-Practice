# 简单选择排序
l = [49, 38, 65, 97, 76, 13, 27, 49]
smaller = 9999
index = 0

# # 第一趟在八个记录中选取关键字最小的，与第一个交换
# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         if l[i] < smaller:
#             smaller = l[i]
#             index = i
#     else:
#         if l[i+1] < smaller:
#             smaller = l[i+1]
#             index = i+1
#
# print(smaller, index)
# l[0] , l[index] = l[index], l[0]
# print(l)
#
# # 第二趟在除了第一个外的七个记录中选取关键字最小的，与第二个交换
# smaller = 9999
# for i in range(1, len(l)-1):
#     if l[i] < l[i+1]:
#         if l[i] < smaller:
#             smaller = l[i]
#             index = i
#     else:
#         if l[i+1] < smaller:
#             smaller = l[i+1]
#             index = i+1
#
# print(smaller, index)
# l[1] , l[index] = l[index], l[1]
# print(l)

# 以此类推，得到简单排序法
for n in range(len(l)):
    smaller = 9999
    for i in range(n, len(l)-1):
        if l[i] < l[i+1]:
            if l[i] < smaller:
                smaller = l[i]
                index = i
        else:
            if l[i+1] < smaller:
                smaller = l[i+1]
                index = i+1

    # print(smaller, index)
    l[n], l[index] = l[index], l[n]
print(l)

