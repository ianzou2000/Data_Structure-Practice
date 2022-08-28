# 栈的顺序实现 及 十进制转二进制
# coding:utf-8


class SeqStack(object):
    def __init__(self, max=5):
        self.max = max  # 默认顺序栈最多容纳5个元素
        self.data = [None] * self.max
        self.top = 0
        self.bottom = 0

    def is_empty(self):  # 判定顺序栈是否为空
        return self.top is 0

    def is_full(self):  # 判定顺序栈是否全满
        return self.top is self.max

    # 获取顺序栈中某一位置的元素
    def __getitem__(self, i):
        if not isinstance(i, int):  # 如果i不为int型，则判定输入有误，即Type错误
            raise TypeError
        if 0 <= i < self.top:  # 如果位置i满足条件，即在元素个数的范围内，则返回相对应的元素值，否则，超出索引，返回IndexError
            return self.data[i]
        else:
            raise IndexError

    # 统计顺序栈中元素的个数
    def Count(self):
        return self.top

    # 栈末尾插入操作(与栈满元素后自动添加的实现)
    def push(self, value):
        if self.top >= self.max:
            # print("The list is full, but I have increased the space.")  # 满了就提示一下。
            self.max += 1  # 实际上这里也可以不用我来自己添加空间了，.append()可以自己分配更大的空间。
            # print(self.max) （调试用）
            self.data.append(value)
            self.top += 1
            return
        else:
            self.data[self.top] = value
            self.top += 1

    # 将栈顶弹出并删除
    def pop(self):
        if self.top == self.bottom:
            raise IndexError
        topValue = self.data[self.top-1]
        self.top -= 1
        self.data[self.top] = None
        return topValue

    # 得到栈顶
    def getTop(self):
        if self.top == self.bottom:
            raise IndexError
        topValue = self.data[self.top-1]
        return topValue

    # 输出操作
    def printStack(self):
        n = self.top  # 这里不能直接用 self.top 去找，不然相当于删除操作。【有点疑问】
        while n > self.bottom:
            n -= 1
            print(self.data[n], end='')
        print('\n')

    # 销毁操作
    def destroy(self):
        self.__init__()

# 线性栈的十进制转二进制
def ten_to_two(value):  # 十进制转二进制
    NumStack = SeqStack()  # 先创建一个线性栈
    left_value = value
    if value != 0:  # 先排除是0的情况
        while left_value > 0:
            Num = left_value % 2  # 除2取余
            NumStack.push(int(Num))
            left_value = left_value / 2
            left_value = int(left_value)  # 这一步需要保证最后一步得到的不是小数，故用int函数可以向下取整。
        NumStack.printStack()
    else:
        print("After transforming: 0")


ten_to_two(198)
ten_to_two(2005)
ten_to_two(10)



