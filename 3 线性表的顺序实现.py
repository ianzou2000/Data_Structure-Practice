# coding:utf-8


class SeqList(object):
    def __init__(self, max=5):
        self.max = max  # 默认顺序表最多容纳5个元素
        self.num = 0
        self.data = [None] * self.max

    def is_empty(self):  # 判定线性表是否为空
        return self.num is 0

    def is_full(self):  # 判定线性表是否全满
        return self.num is self.max

    # 获取线性表中某一位置的元素
    def __getitem__(self, i):
        if not isinstance(i, int):  # 如果i不为int型，则判定输入有误.
            raise TypeError
        if 0 <= i < self.num:  # 如果位置i在元素个数的范围内，则返回相对应的元素值。若超出索引，返回IndexError.
            return self.data[i]
        else:
            raise IndexError

    # 修改线性表种某一位置的元素
    def __setitem__(self, key, value):
        if not isinstance(key, int):  # 如果key不为int型，则判定输入有误，即Type错误
            raise TypeError
        if 0 <= key < self.num:  # 如果位置key在元素个数的范围内，则返回相对应的元素值. 若超出索引，返回IndexError.
            self.data[key] = value
        else:
            raise IndexError

    # 按值查找元素的位置
    def getLoc(self, value):
        for j in range(self.num):
            if self.data[j] == value:
                return j
        else:
            return -1  # 若遍历完了还是没找到该元素，则返回-1.

    # 统计线性表中元素的个数
    def Count(self):
        return self.num

    # 表末尾插入操作(与列表满元素后自动添加的实现)
    def appendLast(self, value):
        if self.num >= self.max:
            print("The list is full, but I have increased the space.")  # 满了就提示一下。
            self.max += 1  # 实际上这里也可以不用我来自己添加空间了，.append()可以自己分配更大的空间。
            # print(self.max) （调试用）
            self.data.append(value)  # 感觉这里像是开挂了，直接用python里列表自带的方法，不禁感叹用python学数据结构有点偷懒。
            self.num += 1
            return
        else:
            self.data[self.num] = value
            self.num += 1

    # 表任意位置插入操作：
    def insert(self, i, value):
        self.num += 1
        if not isinstance(i, int):
            raise TypeError
        if i < 0 or i > self.num:
            raise IndexError
        for j in range(self.num, i, -1):  # 从末端开始一个一个往后挪。
            self.data[j] = self.data[j - 1]
        self.data[i] = value  # 挪完了插入。

    # 删除某一位置的操作
    def remove(self, i):
        if not isinstance(i, int):
            raise TypeError
        if i < 0 or i >= self.num:
            raise IndexError
        for j in range(i - 1, self.num - 1):
            self.data[j] = self.data[j + 1]
        self.num -= 1

    # 输出操作
    def printList(self):
        for i in range(0, self.num):
            print(self.data[i])

    # 销毁操作
    def destroy(self):
        self.__init__()


s = SeqList(5)
s.appendLast(627)
s.appendLast(630)
s.appendLast(655)
s.appendLast(700)
s.appendLast(615)
s.appendLast(500)


s.printList()