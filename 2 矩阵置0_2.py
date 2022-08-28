lists = [[1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 0, 4, 5, 6]]

R = len(lists)  # 统计行数
C = len(lists[0])  # 统计列数，固定一个行再统计列


r = []  # 定义一个空列表接受 0 的 所在 行
c = []  # 定义一个空列表接受 0 的 所在 列


for i in range(R):  # 对行遍历，循环次数为行数
    for j in range(C):  # 对每一行的 每一个列 依次遍历
        if lists[i][j] == 0:  # 检索0元素
            r.append(i)  # 记录 行
            c.append(j)  # 记录 列


for i in range(R):  # 遍历矩阵的每一行
    for j in range(C):  # 遍历某一行的每一个列
        if i in r or j in c:  # 如果这个 行 或 列 在记录的列表中，则执行 置0 操作。
            lists[i][j] = 0


print(lists)